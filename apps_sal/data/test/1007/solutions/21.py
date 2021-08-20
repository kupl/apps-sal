(k, p) = [int(i) for i in input().split()]
ans = 0
for i in range(1, k + 1):
    tmp = str(i)
    n = len(tmp)
    rev = tmp[::-1]
    ans += (i * 10 ** n + int(rev)) % p
print(ans % p)
