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


'''
class Solution:
    def countTriplets(self, A: List[int]) -> int:
        dic = defaultdict(int)
        res = 0
        for i in range(len(A)):
            for j in range(len(A)):
                num = A[i] & A[j]
                dic[num] += 1
        for i in range(len(A)):
            for j in dic:
                if A[i] & j == 0:
                    res += dic[j]
        return res
'''
