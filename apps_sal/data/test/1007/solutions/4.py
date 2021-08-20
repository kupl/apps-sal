(k, p) = map(int, input().split())
ans = 0
for i in range(1, k + 1):
    n = i
    n = str(i) + str(i)[::-1]
    n = int(n)
    ans += n
print(ans % p)
