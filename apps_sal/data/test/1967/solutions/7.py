(n, m) = list(map(int, input().split(' ')))
a = ['' for i in range(m)]
for i in range(m):
    a[i] = input()


def printImage(table):
    for s in table:
        ans = ''
        for c in s:
            ans += c * 2
        print(ans)
        print(ans)


b = []
for i in range(n):
    ans = ''
    for s in a:
        ans += s[i]
    b.append(ans)
printImage(b)
