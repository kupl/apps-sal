def main():
    (n, m) = list(map(int, input().split()))
    remain = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    stack = []
    for i in range(n):
        stack.append((cost[i], i))
    stack.sort()
    stack.reverse()
    for i in range(m):
        (t, d) = list(map(int, input().split()))
        cst = 0
        if remain[t - 1] >= d:
            remain[t - 1] -= d
            cst += d * cost[t - 1]
        else:
            r = d - remain[t - 1]
            cst += remain[t - 1] * cost[t - 1]
            remain[t - 1] = 0
            while r != 0:
                if not stack:
                    cst = 0
                    break
                c = stack.pop()
                if remain[c[1]] >= r:
                    cst += r * cost[c[1]]
                    remain[c[1]] -= r
                    r = 0
                    if remain[c[1]] > 0:
                        stack.append(c)
                else:
                    r -= remain[c[1]]
                    cst += remain[c[1]] * cost[c[1]]
                    remain[c[1]] = 0
        print(cst)


main()
