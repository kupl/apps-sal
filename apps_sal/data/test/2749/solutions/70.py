h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
R = []
for i in range(n):
    for j in range(a[i]):
        R.append(i + 1)
E = []
for i in range(h):
    E.append(R[i * w:(i * w) + w])
for i in range(h):
    if i % 2:
        print(" ".join(map(str, reversed(E[i]))))
    else:
        print(" ".join(map(str, E[i])))
