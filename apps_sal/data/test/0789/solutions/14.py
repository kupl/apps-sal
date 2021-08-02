s = input().strip()
ans = 0
st = 1
for i in range(len(s) - 1, -1, -1):
    if s[i] == '4':
        ans += st
    elif s[i] == '7':
        ans += st * 2
    st *= 2
print(ans)
