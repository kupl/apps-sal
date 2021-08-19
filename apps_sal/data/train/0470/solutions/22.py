class Solution:

    def threeSumMulti(self, A: List[int], target: int) -> int:
        A.sort()
        leftDict = defaultdict(int)
        rightDict = Counter(A[1:])
        ALen = len(A)
        MOD = 10 ** 9 + 7
        leftDict[A[0]] += 1
        ans = 0
        for i in range(1, ALen - 1):
            Ai = A[i]
            rightDict[Ai] -= 1
            for left in leftDict:
                ans += leftDict[left] * rightDict[target - Ai - left]
            leftDict[Ai] += 1
            ans %= MOD
        return ans
