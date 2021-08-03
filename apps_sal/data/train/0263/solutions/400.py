class Solution:
    def knightDialer(self, N: int) -> int:
        possible_ways = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        remember_dict = {}

        def numofways(N, startnum):
            if (startnum, N) in remember_dict:
                return remember_dict[(startnum, N)]
            if N == 1:
                return 1
            else:
                temp = 0
                for nextnum in possible_ways[startnum]:
                    temp += numofways(N - 1, nextnum)
                remember_dict[(startnum, N)] = temp
                return temp
        summation = 0
        for i in range(10):
            summation += numofways(N, i)
        return summation % 1000000007
