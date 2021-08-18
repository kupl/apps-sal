n, m = list(map(int, input().split()))
s = [0] * m
c = [0] * m
d = dict()
ans = 0

for x in range(m):
    s[x], c[x] = list(map(int, input().split()))
    if s[x] not in d:
        d[s[x]] = c[x]
    elif d[s[x]] != c[x]:
        ans = -1
        break

else:
    ans = ""
    for x in range(1, n + 1):
        if x in d:
            if x != 1:
                ans += str(d[x])
            elif x == 1 and d[x] != 0:
                ans += str(d[x])
            elif n == 1 and d[x] == 0:
                ans += "0"
            else:
                ans = -1
                break
        else:
            if m != 0:
                if x == 1:
                    ans += str(1)
                else:
                    ans += str(0)
            else:
                if n == 1:
                    ans = str(0)
                else:
                    ans = "1" + ("0" * (n - 1))

print(ans)
