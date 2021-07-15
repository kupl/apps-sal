class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        
        self.counter = float('inf')
        A = list(A)
        B = list(B)
        
        def swap(first, cur):
            if first == len(A) - 1 or A[first:] == B[first:]:
                self.counter = min(self.counter, cur)
                #print(f'cur={cur}, first={first}')
                return
            for i in range(first, len(A)):
                if A[i] != B[i]:
                    for k in range(i + 1, len(A)):
                        if A[i] == B[k] and cur + 1 < self.counter:
                            B[i], B[k] = B[k], B[i]
                            #print(f'B={B}')
                            swap(i + 1, cur + 1)
                            B[i], B[k] = B[k], B[i]
                    break
            return 
            
        swap(0, 0)
        return self.counter

