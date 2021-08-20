class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        if len(set(arr)) == 1:
            return 1
        if len(set(arr)) == len(arr):
            if len(arr) % 2 == 0:
                return int(len(arr) / 2)
            else:
                return len(arr) // 2 + 1
        u = list(set(arr))
        d_u = {}
        for ele in u:
            d_u[ele] = arr.count(ele)
        d_u = sorted(list(d_u.items()), key=lambda x: x[1], reverse=True)
        s = 0
        size = 0
        for ele in d_u:
            size += 1
            s += ele[1]
            if (s >= len(arr) / 2) & (len(arr) % 2 == 0):
                return size
            if (len(arr) % 2 == 1) & (s >= len(arr) // 2 + 1):
                return size
