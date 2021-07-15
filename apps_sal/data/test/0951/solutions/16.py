k = int(input())
n = sorted(map(int, input()))
s = sum(n)
ans = 0
nk = 0
k = k - s
while nk < k and ans < len(n):
    nk += 9 - n[ans]
    ans += 1
print(ans)
