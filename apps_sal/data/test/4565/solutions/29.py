n = int(input())
s = input()
l = [0] * n
r = [0] * n
ans = n
for i in range(n):
    if i == 0:
        if s[0] == "W":
            l[0] = 1
    elif s[i] == "W":
        l[i] = l[i - 1] + 1
    else:
        l[i] = l[i - 1]
    if i == 0:
        if s[-1] == "E":
            r[0] = 1
    elif s[-i-1] == "E":
        r[i] = r[i - 1] + 1
    else:
        r[i] = r[i - 1]
for i in range(n):
    if i == 0:
        ans = min(ans, r[n - 1 - i])
    elif i == n - 1:
        ans = min(ans, l[i - 1])
    else:
        ans = min(ans, l[i - 1] + r[n - 1 - i])
print(ans)
