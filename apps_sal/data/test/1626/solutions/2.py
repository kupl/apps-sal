# import sys
# n = int(input())
# s = input().strip()
# a = [int(tmp) for tmp in input().split()]
# for i in range(n):
n, k = [int(tmp) for tmp in input().split()]
a = [int(tmp) for tmp in input().split()]
b = [int(tmp) for tmp in input().split()]
BIG = 10 ** 9 + 7
m = n // k
ans = [0] * m
for i in range(m):
    ans[i] = (10 ** k + a[i] - 1) // a[i]
    x = 10 ** (k - 1) * b[i] % a[i]
    if x != 0:
        ans[i] -= (10 ** (k - 1) + x + a[i] - 1) // a[i] - 1
    else:
        ans[i] -= (10 ** (k - 1) + x + a[i] - 1) // a[i]
all_ans = 1
for i in range(m):
    all_ans = (all_ans * ans[i]) % BIG
print(all_ans)
