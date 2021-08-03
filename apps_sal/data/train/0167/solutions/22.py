class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        self.memo = {}

        return self.cal_eggs(K, N)

    def find_that_floor(self, K, N):
        left, right = 1, N
        while (left <= right):
            mid = (left + right) // 2
            # if it breaks;
            r1 = 1 + self.cal_eggs(K - 1, mid - 1)
            # if it not breaks;
            r2 = 1 + self.cal_eggs(K, N - mid)

            if r1 == r2:
                return mid
            elif r1 < r2:
                left = mid + 1
            else:
                right = mid - 1

        return right

    def cal_eggs(self, K, N):
        # print(K,N)
        if N == 0:
            return 0
        if K == 1:
            return N

        if (K, N) not in self.memo:
            r = 2 ** 32 - 1
            now_floor = self.find_that_floor(K, N)
            for floor in range(now_floor, min(now_floor + 2, N + 1)):
                # if it breaks;
                r1 = 1 + self.cal_eggs(K - 1, floor - 1)
                # if it not breaks;
                r2 = 1 + self.cal_eggs(K, N - floor)

                r = min(r, max(r1, r2))

            self.memo[(K, N)] = r

        return self.memo[(K, N)]
