k, r = map(int, input().split())
ans = 1
c = k
while k % 10 != 0 and (k - r) % 10 != 0:
    ans += 1
    k += c
print(ans)
