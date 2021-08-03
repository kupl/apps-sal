H = int(input())
c = 1
ans = 1
while H > 1:
    H //= 2
    c *= 2
    ans += c
print(ans)
