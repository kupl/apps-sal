n = int(input())
s = str(input())
ans = 0
for i in range(1, n):
    l = list(s[0:i])
    r = list(s[i:n])
    dup = len(set(l) & set(r))
    if ans < dup:
        ans = dup
print(ans)
