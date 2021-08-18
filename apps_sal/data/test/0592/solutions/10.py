
"""

created by shuangquan.huang at 11/19/18

"""

N = int(input())

ans = 0
for i in range(2, N + 1):
    ans += 4 * i * (N // i - 1)
print(ans)
