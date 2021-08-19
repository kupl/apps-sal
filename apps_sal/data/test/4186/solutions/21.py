# alpha = "abcdefghijklmnopqrstuvwxyz"
t = 1  # int(input())
for test in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = [-a[2 * i] + a[2 * i + 1] for i in range(n // 2)]
    print(sum(ans))
