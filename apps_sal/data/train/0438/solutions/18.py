class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        f = [ii for ii in range(n)]     # union find
        b = [0 for ii in range(n)]      # whether turns to 1
        s = [0 for ii in range(n)]      # sum

        def findunion(n):
            if f[n] == n:
                return n
            else:
                f[n] = findunion(f[n])
                return f[n]

        ans = -1
        m_set = 0
        for i in range(len(arr)):
            item = arr[i] - 1
            b[item] = 1
            s[item] = 1
            tmp = 1

            if item < n - 1 and b[item + 1] == 1:
                f[item + 1] = item
                s[item] = s[item + 1] + 1
                if s[item + 1] == m:
                    m_set -= 1
                tmp = s[item]

            if item > 0 and b[item - 1] == 1:
                fa = findunion(item - 1)
                f[item] = fa
                if s[fa] == m:
                    m_set -= 1
                s[fa] = s[item] + s[fa]
                tmp = s[fa]

            if tmp == m:
                m_set += 1
            if m_set > 0:
                ans = i + 1

        return ans
