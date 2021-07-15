class Solution:
    def findLatestStep(self, A, m):
        length = [0] * (len(A) + 2)
        count = [0] * (len(A) + 1)
        res = -1
        for i, a in enumerate(A):
            left, right = length[a - 1], length[a + 1]
            length[a] = length[a - left] = length[a + right] = left + right + 1
            count[left] -= 1
            count[right] -= 1
            count[length[a]] += 1
            if count[m]:
                res = i + 1
        return res        
