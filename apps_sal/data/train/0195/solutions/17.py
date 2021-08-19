class Solution:

    def countTriplets(self, A: List[int]) -> int:
        dic = defaultdict(int)
        res = 0
        for i in A:
            for j in A:
                tmp = i & j
                dic[tmp] += 1
        for i in A:
            for j in dic:
                if i & j == 0:
                    res += dic[j]
        return res


'\nclass Solution:\n    def countTriplets(self, A: List[int]) -> int:\n        dic = defaultdict(int)\n        res = 0\n        for i in range(len(A)):\n            for j in range(len(A)):\n                num = A[i] & A[j]\n                dic[num] += 1\n        for i in range(len(A)):\n            for j in dic:\n                if A[i] & j == 0:\n                    res += dic[j]\n        return res\n'
