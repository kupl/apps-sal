for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = [a[0]] + [a[i] for i in range(1, n - 1) if not (a[i - 1] < a[i] < a[i + 1] or a[i - 1] > a[i] > a[i + 1])] + [a[-1]]
    print(len(b))
    print(*b)
