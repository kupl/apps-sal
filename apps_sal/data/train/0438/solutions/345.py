import copy


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        opts = [i for i in range(n + 1)]
        if m > n:
            return -1
        if m == n:
            return n
        (left, right) = ([i for i in range(n + 2)], [i for i in range(n + 2)])

        def find_l(node):
            if left[node] != node:
                left[node] = find_l(left[node])
            return left[node]

        def find_r(node):
            if right[node] != node:
                right[node] = find_r(right[node])
            return right[node]
        ret = -1
        cnt = collections.defaultdict(int)
        for (i, ind) in enumerate(arr):
            left[ind] = l_par = find_l(ind - 1)
            right[ind] = r_par = find_r(ind + 1)
            if ind - l_par == 1 and r_par - ind == 1:
                cnt[1] += 1
            elif ind - l_par != 1 and r_par - ind != 1:
                l_dis = ind - l_par - 1
                r_dis = r_par - ind - 1
                cnt[l_dis] -= 1
                if cnt[l_dis] == 0:
                    del cnt[l_dis]
                cnt[r_dis] -= 1
                if cnt[r_dis] == 0:
                    del cnt[r_dis]
                cnt[l_dis + r_dis + 1] += 1
            else:
                dis = 0
                if ind - l_par == 1:
                    dis = r_par - ind
                elif r_par - ind == 1:
                    dis = ind - l_par
                cnt[dis - 1] -= 1
                if cnt[dis - 1] == 0:
                    del cnt[dis - 1]
                cnt[dis] += 1
            if m in cnt:
                ret = i + 1
        return ret
