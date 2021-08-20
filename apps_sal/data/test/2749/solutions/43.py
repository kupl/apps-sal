(h, w) = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
l = []
for i in range(len(a)):
    l += [i + 1] * a[i]
for i in range(h):
    if i % 2 == 0:
        print(*l[i * w:(i + 1) * w])
    else:
        print(*list(reversed(l[i * w:(i + 1) * w])))
