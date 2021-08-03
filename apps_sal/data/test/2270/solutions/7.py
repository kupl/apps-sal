mod = 998244353
n = int(input())
a = list(map(int, input().split()))
d = dict()
two = 0
four = 0
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in d:
    two += d[i] // 2
    four += d[i] // 4
m = int(input())
for i in range(m):
    s = input().split()
    if s[0] == '+':
        l = int(s[1])
        if l in d:
            d[l] += 1
        else:
            d[l] = 1
        if d[l] % 2 == 0:
            two += 1
        if d[l] % 4 == 0:
            four += 1
    else:
        l = int(s[1])
        d[l] -= 1
        if d[l] % 2 == 1:
            two -= 1
        if d[l] % 4 == 3:
            four -= 1
    if four > 0 and two > 3:
        print("YES")
    else:
        print("NO")
