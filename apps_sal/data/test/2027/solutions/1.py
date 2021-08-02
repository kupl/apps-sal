n = int(input())
l = list(map(int, input().split()))
a = []
a += [l[-1]]
for i in range(n - 1, 0, -1):
    a += [l[i] + l[i - 1]]
a = a[::-1]
print(' '.join(list(map(str, a))))
