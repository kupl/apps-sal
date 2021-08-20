import sys
input = sys.stdin.readline
for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if len(set(a)) > k:
        print(-1)
        continue
    a = list(set(a))
    a += [1] * (k - len(a))
    print(k * n)
    print(*a * n)
