import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
sol = [-1] * n
touse = list(range(n + 1))
if a[0] == 1:
    sol[0] = 0
    touse[0] = -1
for i in range(1, n):
    if a[i] > a[i - 1]:
        sol[i] = a[i - 1]
        touse[a[i - 1]] = -1
j = 0
touse[a[-1]] = -1
for i in range(n):
    if sol[i] == -1:
        while touse[j] == -1:
            j += 1
        sol[i] = touse[j]
        j += 1
print(*sol)
