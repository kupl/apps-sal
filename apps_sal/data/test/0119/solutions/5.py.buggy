import sys


def inn(a, b):
    return (a[0] <= b[0] and b[1] <= a[1])


n = int(input())

seg = []

a, b = map(int, input().split())
seg.append((a, b, 1))

for i in range(2, n + 1):
    a, b = map(int, input().split())
    seg.append((a, b, i))

seg.sort(key=lambda x: (x[0], -x[1]))

main = seg.pop(0)

for i in seg:
    if inn(main, i):
        print(i[2], main[2])
        return
    if main[1] < i[1]:
        main = i

print(-1, -1)
