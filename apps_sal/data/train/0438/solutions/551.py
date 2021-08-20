class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        '\n        group_edge = [0] * (len(arr)+2)\n        ans = 0 \n        for i in range(0, len(arr)):\n            print(arr[i])\n            left=right=arr[i]\n            if group_edge[right+1]>0: \n                right=group_edge[right+1]\n            if group_edge[left-1]>0: \n                left=group_edge[left-1]\n            group_edge[left], group_edge[right] = right, left\n            if (right-arr[i]==m) or (arr[i]-left ==m): \n                ans=i\n            print(group_edge)\n        '
        group_len = [0] * (len(arr) + 2)
        cnt_group_len = [0] * (len(arr) + 1)
        ans = -1
        for i in range(0, len(arr)):
            left_most = arr[i] - 1
            right_most = arr[i] + 1
            new_len = group_len[left_most] + group_len[right_most] + 1
            group_len[arr[i]] = new_len
            cnt_group_len[new_len] += 1
            cnt_group_len[group_len[left_most]] -= 1
            cnt_group_len[group_len[right_most]] -= 1
            if group_len[left_most] > 0:
                group_len[arr[i] - group_len[left_most]] = new_len
            if group_len[right_most] > 0:
                group_len[arr[i] + group_len[right_most]] = new_len
            if cnt_group_len[m] > 0:
                ans = i + 1
        return ans
