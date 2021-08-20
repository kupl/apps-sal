class Solution:

    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        even = {}
        odd = {}
        stack = []
        ascending_idx = sorted([i for i in range(n)], key=lambda i: A[i])
        for idx in ascending_idx:
            while stack and idx > stack[-1]:
                odd[stack.pop()] = idx
            stack.append(idx)
        stack = []
        descending_idx = sorted([i for i in range(n)], key=lambda i: -A[i])
        for idx in descending_idx:
            while stack and idx > stack[-1]:
                even[stack.pop()] = idx
            stack.append(idx)
        del stack
        res = 0
        for key in list(odd.keys()):
            if odd[key] == n - 1:
                res += 1
            else:
                nxt = odd[key]
                (jumps, other) = (0, even)
                while nxt in other:
                    jumps += 1
                    nxt = even[nxt] if jumps % 2 != 0 else odd[nxt]
                    if nxt == n - 1:
                        res += 1
                        break
                    other = even if jumps % 2 == 0 else odd
        return res + 1
