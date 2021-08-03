n = int(input())
H = list(map(int, input().split()))
chk = 0
M = 0
for i in range(n - 1):
    if H[i + 1] <= H[i]:
        chk += 1
    else:
        M = max(M, chk)
        chk = 0
print(max(M, chk))
