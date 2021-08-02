n = int(input())
s = 100
ans = 0
while s < n:
    s += s // 100
    ans += 1
print(ans)
