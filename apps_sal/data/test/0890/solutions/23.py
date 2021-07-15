def f(k, n, ma, mi, sum):
    if k:
        if sum + k[0] <= r and sum + k[0] >= l and   max(k[0], ma) - min(k[0], mi) >= x:
            n+=1
        if sum <= r:
            n = f(k[1:], n, ma, mi, sum)
            n = f(k[1:], n, max(k[0], ma), min(k[0], mi), sum + k[0])
    return n
n, l, r, x = [int(i) for i  in input().split()]
s = [int(i) for i  in input().split()]
n = f(s, 0, 0, 10**9, 0)
print(n)

