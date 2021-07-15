class Solution:
    def knightDialer(self, n: int) -> int:
        dialer = {}
        for i in range(10):
            dialer[i] = 1
        for j in range(n):
            store = [dialer[k] for k in dialer]
            dialer[0] = store[4] + store[6]
            dialer[1] = store[8] + store[6]
            dialer[2] = store[9] + store[7]
            dialer[3] = store[8] + store[4]
            dialer[4] = store[0] + store[9] + store[3]
            dialer[5] = 0
            dialer[6] = store[0] + store[7] + store[1]
            dialer[7] = store[2] + store[6]
            dialer[8] = store[1] + store[3]
            dialer[9] = store[2] + store[4]
        return sum(store) % (10 ** 9 + 7)
