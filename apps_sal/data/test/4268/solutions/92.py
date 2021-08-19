def calc(D, a, b):
    d2 = 0
    for i in range(D):
        d2 += abs(a[i] - b[i]) ** 2
    return d2 ** 0.5


(N, D) = map(int, input().split())
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        d = calc(D, lst[i], lst[j])
        if int(d) == d:
            ans += 1
print(ans)
