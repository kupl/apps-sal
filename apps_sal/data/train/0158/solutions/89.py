class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        queue = collections.deque([(A, 0, 0)])
        s = {A}
        
        while queue:
            curr_A, curr_k, curr_p = queue.popleft()
            # print(curr_A, curr_k, curr_p)
            if curr_A == B:
                return curr_k
            for i in range(curr_p, len(A)):
                if curr_A[i] != B[i]:
                    for j in range(i+1, len(A)):
                        if curr_A[j] == B[i] and curr_A[:i] + curr_A[j] + curr_A[i+1: j] + curr_A[i] + curr_A[j+1:] not in s:
                            queue.append((curr_A[:i] + curr_A[j] + curr_A[i+1: j] + curr_A[i] + curr_A[j+1:], curr_k + 1, i + 1))
                            s.add(curr_A[:i] + curr_A[j] + curr_A[i+1: j] + curr_A[i] + curr_A[j+1:])
                    break
            

