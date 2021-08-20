def show():
    for i in range(n):
        print(' '.join([str(s) for s in a[i]]))


(n, k) = [int(s) for s in input().split()]
a = [[0 for i in range(n)] for j in range(n)]
if k > n ** 2:
    print(-1)
elif k == 0:
    show()
else:
    for i in range(n):
        if k > 0:
            a[i][i] = 1
            k -= 1
            t = i
            while k >= 2 and t < n - 1:
                t += 1
                a[i][t] = 1
                a[t][i] = 1
                k -= 2
        else:
            break
    show()
