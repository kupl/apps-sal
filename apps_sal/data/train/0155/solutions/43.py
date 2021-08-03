class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        arr.append(math.inf)  # 让所有元素都出栈
        dp = [1] * len(arr)
        stack = []  # 单调递减栈
        for i, cur in enumerate(arr):
            while stack and arr[stack[-1]] < cur:
                poped_same_val = [stack.pop()]
                while stack and arr[stack[-1]] == arr[poped_same_val[0]]:  # val一样的元素，他们的right_first_bigger和left_first_bigger都是一样的，要一起拿出来更新。
                    poped_same_val.append(stack.pop())
                for poped in poped_same_val:
                    if i - poped <= d:  # i是poped的右侧第一个相等或更大的元素
                        dp[i] = max(dp[i], dp[poped] + 1)
                    if stack and poped - stack[-1] <= d:  # stack[-1]是poped的左侧第一个更大的元素
                        left_first_big_of_poped = stack[-1]
                        dp[left_first_big_of_poped] = max(dp[left_first_big_of_poped], dp[poped] + 1)
            stack.append(i)
            # print(i, dp, stack)
        return max(dp[:-1])  # 去掉最后一个inf在的位置的dp值
