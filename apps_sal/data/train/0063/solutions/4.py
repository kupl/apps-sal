ans = []
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    u = list(map(int, input().split()))
    w = list(map(int, input().split()))
    u.sort()
    w.sort(reverse=1)
    ansi = 0
    ind = 0
    for i in range(k):
        if w[i] == 1:
            ansi += u[n - k + i] * 2
        else:
            ansi += u[ind] + u[n - k + i]
        ind += w[i] - 1
    ans.append(ansi)
print('\n'.join(map(str, ans)))
