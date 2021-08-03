'''
ABC066 A - ringring
https://atcoder.jp/contests/abc066/tasks/abc066_a
'''
nums = list(map(int, input().split()))
ans = sum(nums) - max(nums)
print(ans)
