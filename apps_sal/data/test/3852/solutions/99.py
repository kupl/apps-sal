n = int(input())
al = list(map(int, input().split()))
amax = -10 ** 7
maxi = -1
amin = 10 ** 7
mini = -1
for (i, a) in enumerate(al):
    if a > amax:
        amax = a
        maxi = i
    if a < amin:
        amin = a
        mini = i
ansl = []
if amin >= 0 or amax >= abs(amin):
    print(2 * n - 1)
    for i in range(n):
        print(maxi + 1, i + 1)
    for i in range(n - 1):
        print(i + 1, i + 2)
else:
    print(2 * n - 1)
    for i in range(n):
        print(mini + 1, i + 1)
    for i in range(n - 1, 0, -1):
        print(i + 1, i)
