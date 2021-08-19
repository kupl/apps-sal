def check(s, n):
    ans = 0
    if s != '':
        ans = int(s)
    return ans < n


n = int(input())
k = input()
s = ''
i = len(k) - 1
ans = 0
add = 1
while i >= 0:
    while i >= 0 and check(k[i] + s, n):
        s = k[i] + s
        i -= 1
    while len(s) > 1 and s[0] == '0':
        s = s[1:]
        i += 1
    ans += int(s) * add
    add *= n
    s = ''
print(ans)
