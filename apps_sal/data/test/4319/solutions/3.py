def mi():
    return map(int, input().split())


n = int(input())
a = list(mi())
c = []
for i in range(1, n):
    if a[i] == 1:
        c.append(a[i - 1])
c.append(a[-1])
print(len(c))
for i in c:
    print(i, end=' ')
