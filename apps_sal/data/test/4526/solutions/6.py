for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    special = [0] * (2 * n)
    for i in range(n - 1):
        summ = a[i]
        j = i + 1
        while j < n and summ < n:
            summ += a[j]
            j += 1
            special[summ] = 1
    cnt_spec = 0
    for i in range(n):
        cnt_spec += special[a[i]]
    print(cnt_spec)
