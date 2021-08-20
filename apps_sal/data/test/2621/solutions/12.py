for t in range(int(input())):
    (n, m, k) = map(int, input().split())
    l = list(map(int, input().split()))
    dep = m
    for i in range(n - 1):
        if l[i + 1] > l[i] + k:
            need = l[i + 1] - (l[i] + k)
            if need > dep:
                print('NO')
                break
            dep -= need
        else:
            dep += min(l[i], l[i] + k - l[i + 1])
    else:
        print('YES')
