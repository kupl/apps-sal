n, k = list(map(int, input().split()))
s = list(map(int, input().split()))
c = 0
for i in range(n):
    if s[i] <= k:
        c += 1
    else:
        break
for i in range(n - c):
    if s[n - 1 - i] <= k:
        c += 1
    else:
        break
print(c)
