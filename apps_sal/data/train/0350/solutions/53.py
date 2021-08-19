class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        left1 = 0
        left2 = 0
        w1 = {}
        w2 = {}
        count = 0
        for (right, x) in enumerate(A):
            if x in w1:
                w1[x] += 1
            else:
                w1[x] = 1
            if x in w2:
                w2[x] += 1
            else:
                w2[x] = 1
            while len(w1) > K:
                if w1[A[left1]] == 1:
                    w1.pop(A[left1])
                elif w1[A[left1]] > 1:
                    w1[A[left1]] -= 1
                left1 += 1
            while len(w2) >= K:
                if w2[A[left2]] == 1:
                    w2.pop(A[left2])
                elif w2[A[left2]] > 1:
                    w2[A[left2]] -= 1
                left2 += 1
            count += left2 - left1
        return count
