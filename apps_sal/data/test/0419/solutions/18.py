s = int(input(), 2)
ans = 0
k = 1
while k < s:
    ans += 1
    k *= 4
print(ans)
