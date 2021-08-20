(n, s) = input().split()
last = s[0]
ans = n[0]
for x in n[1:]:
    if x < last:
        ans += x
    else:
        break
print(ans + last)
