n = int(input())
d = list(map(int, input().split()))
d = sorted(d)
n2 = int(n / 2)
if d[n2] == d[n2 - 1]:
    print(0)
else:
    print(d[n2] - d[n2 - 1])
