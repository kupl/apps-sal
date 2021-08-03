n = int(input())
ans = 0
for i in range(1, n + 1):
    j = n // i
    ans += j * (j + 1) * i / 2
print(int(ans))
