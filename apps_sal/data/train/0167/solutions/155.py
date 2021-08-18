class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dict_soln = {}
        return self.dp(K, N, dict_soln)

    def dp(self, k, n, dict_soln):
        if n == 0:
            return 0
        if k == 0:
            return -1
        if k == 1:
            return n
        if (k, n) in dict_soln:
            return dict_soln[(k, n)]
        left = 1
        right = n
        while True:
            if left - right == -1:
                tmp1 = self.dp(k - 1, left - 1, dict_soln)
                tmp2 = self.dp(k, n - left, dict_soln)
                tmp3 = self.dp(k - 1, right - 1, dict_soln)
                tmp4 = self.dp(k, n - right, dict_soln)
                tmpl = max(tmp1, tmp2)
                tmpr = max(tmp3, tmp4)
                if tmpl < tmpr:
                    dict_soln[(k, n)] = tmpl + 1
                    return dict_soln[(k, n)]
                else:
                    dict_soln[(k, n)] = tmpr + 1
                    return dict_soln[(k, n)]
            xmid = (left + right) // 2
            tmp1 = self.dp(k - 1, xmid - 1, dict_soln)
            tmp2 = self.dp(k, n - xmid, dict_soln)
            if tmp1 > tmp2:
                right = xmid
            elif tmp1 < tmp2:
                left = xmid
            else:
                dict_soln[(k, n)] = tmp1 + 1
                return dict_soln[(k, n)]
