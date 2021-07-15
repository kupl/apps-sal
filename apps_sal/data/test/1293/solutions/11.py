import sys
# динамика!!!
# смотри на ограничения
# for i in range(n):
# n = int(input())
# s = input().split()
# a = [int(tmp) for tmp in input().split()]
n = int(input())
a = [int(tmp) for tmp in input().split()]
ans = 0
now = 0
for i in range(n):
    ans += abs(a[i] - now)
    now += a[i] - now
print(ans)
