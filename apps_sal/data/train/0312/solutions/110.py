class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        mx = sys.maxsize
        if A[0] == K:
            return 1
        for i in range(1, len(A)):
            A[i] += A[i - 1]
            if A[i] >= K:
                mx = min(mx, i + 1)
        st = [0]
        for i in range(1, len(A)):
            while len(st) and A[i] - A[st[0]] >= K:
                popped = st.pop(0)
                mx = min(mx, i - popped)
            while len(st) and A[i] <= A[st[-1]]:
                st.pop()
            st.append(i)
        return mx if mx != sys.maxsize else -1
        "\n        d = []\n        o = []\n        res, cur = float('inf'), 0\n        for i, a in enumerate(A):\n            cur += a\n            o.append(cur)\n            while d and cur - d[0][1] >= K:\n                res = min(res, i - d.pop(0)[0])\n            while d and cur <= d[-1][1]:\n                d.pop()\n            d.append([i, cur])\n        print(o)\n        return res if res < float('inf') else -1\n    "
