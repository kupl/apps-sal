class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        leftMax = A[l]
        rightMin = A[r]
        minHash = {}

        while l < r:
            leftMax = max(leftMax, A[l])
            rightMin = min(rightMin, A[r])

            if rightMin >= leftMax:
                r -= 1
            else:
                l += 1

        for i in range(r, len(A)):
            if A[i] not in minHash:
                minHash[A[i]] = []
            minHash[A[i]].append(i)
        minHash = sorted(list(minHash.items()), key=lambda x: x[0])

        i, res = 0, 1
        while i < len(minHash) and minHash[i][0] < leftMax:
            positions = minHash[i][1]
            res = max(positions[-1] + 1, res)
            i += 1

        return res
