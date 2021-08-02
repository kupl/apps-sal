H = int(input())
for i in range(0, 40):
    if 2**i <= H < 2**(i + 1):
        H = 2 ** i
        break
ans = 0
for k in range(0, i + 1):
    ans += 2**k
print(ans)
