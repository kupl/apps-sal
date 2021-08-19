t = int(input())
for ii in range(t):
    n, p, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a = sorted(a)
    a = [None] + a
    s = [0] * (n + 1)
    last_ind = 0
    for i in range(1, n + 1):
        if i < k:
            s[i] = a[i] + s[i - 1]
        else:
            s[i] = a[i] + s[i - k]
        # print('---',s[i], p)
        if s[i] <= p:
            last_ind = i

    print(last_ind)

'''
8
5 6 2
2 4 3 5 7
5 11 2
2 4 3 5 7
3 2 3
4 2 6
5 2 3
10 1 3 9 2
2 10000 2
10000 10000
2 9999 2
10000 10000
4 6 4
3 2 3 2
5 5 3
1 2 2 1 2

'''
