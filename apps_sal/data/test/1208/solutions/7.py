n = int(input())
ans = 0
k = 0
d = {}
for i in range(n):
    s = input()
    a = int(s[2:])
    if s[0] == '+':
        d[a] = 'yes'
        k += 1
        if k > ans:
            ans = k
    else:
        if a not in d:
            ans += 1
        else:
            d[a] = 'no'
            k -= 1
print(ans)
