from sys import stdin, stdout


n = int(stdin.readline().rstrip())

a = []
b = []
for i in range(n):
    x, y = list(map(int, stdin.readline().rstrip().split()))
    a.append(x)
    b.append(y)

rated = 0
for i in range(n):
    if a[i] != b[i]:
        rated = 1
        break

if not rated:
    for i in range(n - 1):
        if a[i] < a[i + 1]:
            rated = -1

if rated == 1:
    print("rated")
elif rated == 0:
    print("maybe")
else:
    print("unrated")
