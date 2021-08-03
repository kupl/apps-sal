class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        a, b, m = [deque([0] * x) for x in rollMax], [1] * 6, 1000000007
        for x in a:
            x[-1] = 1
        for _ in range(n - 1):
            s = sum(b) % m
            for i, x in enumerate(a):
                x.append((s - b[i]) % m)
                b[i] = (b[i] + x[-1] - x.popleft()) % m
        return sum(b) % m
