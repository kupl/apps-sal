import sys
input = sys.stdin.readline
for nt in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    (o, e) = (0, 0)
    for i in a:
        if i % 2:
            o += 1
        else:
            e += 1
    if o != e and e != o + 1:
        print(-1)
        continue
    count = 0
    for i in range(n):
        if i % 2 != a[i] % 2:
            count += 1
    print(count // 2)
