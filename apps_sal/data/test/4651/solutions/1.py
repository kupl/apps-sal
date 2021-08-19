q = int(input())
for t in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    used = [0] * n
    for i in range(1, n + 1):
        ind = a.index(i)
        while ind > 0 and used[ind - 1] == 0 and (a[ind - 1] > i):
            s = a[ind - 1]
            a[ind] = s
            a[ind - 1] = i
            used[ind - 1] = 1
            ind -= 1
    print(*a)
