class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        def nei(x):
            i = 0
            while x[i] == B[i]: i+=1 #continue incremeneting if characters are same
            for j in range(i+1, len(x)):
                if x[j] == B[i] and x[j] != B[j]:
                    yield x[:i]+x[j]+x[i+1:j]+x[i]+x[j+1:] #swaps the two characters
        q, seen = [(A,0)], {A}

        while q != []:
            x, d = q.pop(0)
            if x == B: return d #return immediately from BFS if the strings are the same
            for y in nei(x):
                #print(\"y\", y)
                if y not in seen:
                    seen.add(y), q.append((y,d+1))
            #print(\"q\", q)

