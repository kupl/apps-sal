class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        list_old = [1] * 10
        for t in range(2, n + 1):
            list_new = [0] * 10
            for i in range(0, 10):
                temp = Solution().map(i)
                for j in range(len(temp)):
                    list_new[i] = list_new[i] + list_old[temp[j]]
            list_old = list_new[0:10]
        return sum(list_old) % (10**9 + 7)

    def map(self, d: int) -> List[int]:
        if d == 0:
            return [4, 6]
        elif d == 1:
            return [6, 8]
        elif d == 2:
            return [7, 9]
        elif d == 3:
            return [4, 8]
        elif d == 4:
            return [0, 3, 9]
        elif d == 5:
            return []
        elif d == 6:
            return [0, 1, 7]
        elif d == 7:
            return [2, 6]
        elif d == 8:
            return [1, 3]
        else:
            return [2, 4]
