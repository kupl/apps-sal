n, m = map(int, input().split())


a = [0] * m
b = [0] * m
c = [0] * m
for i in range(m):
    l, r = input().split()
    a[i] = l
    b[i] = r
    if len(l) <= len(r):
        c[i] = l
    else:
        c[i] = r

s = list(input().split())

answer = ""
for i in range(n):
    if s[i] in a:
        x = a.index(s[i])
    else:
        x = b.index(s[i])
    answer += c[x]
    answer += " "
tr = len(answer)
print(answer[0:tr - 1])
