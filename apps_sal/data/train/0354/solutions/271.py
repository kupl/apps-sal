class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        arr = []
        while n > 0:
            if not arr:
                arr.append([1 for _ in range(6)])
            else:
                cur_turn = [0 for _ in range(6)]
                for i in range(6):
                    if rollMax[i] > len(arr):
                        cur_turn[i] = sum(arr[-1])
                    else:
                        for k in range(1, 1 + rollMax[i]):
                            cur_turn[i] += sum(arr[-k]) - arr[-k][i]
                cur_turn = [c % (10 ** 9 + 7) for c in cur_turn]
                arr.append(cur_turn)
            n -= 1
        return sum(arr[-1]) % (10 ** 9 + 7)
