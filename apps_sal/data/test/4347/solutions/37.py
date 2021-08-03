n = int(input())
ncr = 1
for i in range(n // 2 + 1, n + 1):
    ncr = ncr * i
for i in range(1, n // 2 + 1):
    ncr = ncr // i
ans = ncr // 2
fmul = 1
for i in range(1, n // 2):
    fmul = fmul * i
ans = ans * fmul
ans = ans * fmul
ans = int(ans)
print(ans)
