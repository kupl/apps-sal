class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        index = [0] * (n + 2)
        length = [0] * (n + 1)
        ans = -1
        for i in range(n):
            x = arr[i]
            l_l = index[x - 1]
            r_l = index[x + 1]
            new_l = 1 + l_l + r_l
            index[x] = new_l
            index[x - l_l] = new_l
            index[x + r_l] = new_l
            if length[l_l]:
                length[l_l] -= 1
            if length[r_l]:
                length[r_l] -= 1
            length[new_l] += 1
            if length[m] > 0:
                ans = i + 1
        return ans
