from sys import stdin, stdout
input = stdin.readline
for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    for i in range(k):
        if a[i] >= b[n - i - 1]:
            break
        a[i] = b[n - i - 1]
    print(sum(a))
