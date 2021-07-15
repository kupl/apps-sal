n = int(input())
ans = n//11*2
if 0 < n%11 <= 6:
    ans += 1
elif 6 < n%11 <= 10:
    ans += 2

print(ans)
