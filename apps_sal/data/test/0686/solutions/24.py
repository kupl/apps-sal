from sys import stdin
for _ in range(int(stdin.readline())):
    n, m = list(map(int,stdin.readline().split()))
    if n-m == 1:
        print("NO")
    else:
        print("YES")

