H = int(input())
c = 0
ans = 0
while H > 1:
    H //= 2
    ans += 2**c
    c += 1
ans += 2**c
print(ans)
