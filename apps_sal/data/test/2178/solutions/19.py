n = int(input())
a = list(map(int, input().split()))
a.reverse()
b = list(map(int, input().split()))
u = set()
for i in range(n):
    c = 0
    if not b[i] in u:
        while a[-1] != b[i]:
            u.add(a[-1])
            a.pop()
            c += 1
        u.add(a[-1])
        a.pop()
        c += 1
    print(c, end=' ')
