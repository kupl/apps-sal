class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        def nei(x):
            i = 0
            while x[i]==B[i]:
                i+=1
            for j in range(i+1, len(x)):
                if x[i]==B[j] and x[j] != B[j]: 
                    yield x[:i] + x[j] + x[i+1:j] + x[i] + x[j+1:]
        
        seen = {A}
        queue = [(A,0)]
        for node, change in queue:
            if node==B:
                return change
            for y in nei(node):
                if y not in seen:
                    seen.add(node)
                    queue.append((y, change+1))
