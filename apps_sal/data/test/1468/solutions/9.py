n = int(input())
l = []
for i in range(n):
    l.append(input())


def lexi(i):
    j = 1
    while j < len(l[i]) and l[i - 1][j] == l[i][j]:
        j += 1
    l[i - 1] = l[i - 1][:j]


for i in range(n - 1, 0, -1):
    if l[i - 1] > l[i]:
        lexi(i)
print('\n'.join(l))
