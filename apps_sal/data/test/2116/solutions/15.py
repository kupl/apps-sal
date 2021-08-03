n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))


time = 0


for i in range(n):
    c = list(map(int, input().split()))
    for j in c:
        for k in range(len(a)):
            if a[k] == j:
                p = k
                break
        time += p + 1
        a = [j] + a[:k] + a[k + 1:]

print(time)
