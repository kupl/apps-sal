for i in range(int(input())):
    m, k = [int(j) for j in input().split()]
    data = [int(j) for j in input().split()]
    mn = min(data)
    mx = max(data)
    if mx - mn > 2 * k:
        print(-1)
    else:
        print(mn + k)
