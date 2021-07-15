s,p = map(int, input().split())
x = int(p**0.5)
ans = "No"
for a in range(1, x+1):
    if p%a!=0: continue
    b = p//a
    if a+b == s:
        ans = "Yes"
        break
print(ans)
