n = int(input())

cl = list(map(int, input().split()))
cl = sorted(cl)
pos = n // 2

res = 0
for i in range(1, n // 2 + 1):
    res += (cl[n // 2 - i] + cl[n // 2 + i - 1])**2

print(res)
