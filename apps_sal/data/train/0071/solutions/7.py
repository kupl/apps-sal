for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] + a[i]
    print(abs(min(pre)))
