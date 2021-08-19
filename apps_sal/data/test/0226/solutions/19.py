N = int(input())
n = list(map(int, input().split(" ")))

if N == 1:
    ans = [0, n[0]]
elif N == 2:
    ans = [min(n), max(n)]
else:
    # print(n)
    n.reverse()
    f = max(n[0], n[1])  # f2
    s = n[0] + n[1]  # s2
    for i in range(2, N):
        f = max(n[i] + s - f, f)
        s += n[i]
    # print(f)
    # print(s)
    ans = [s - f, f]

print(" ".join(map(str, ans)))

# assume f(n) is the optimal strategy for the remaning n pies, x_n, x_n-1, ...., x_1
#
# s(n) = sum(x_1,..., x_n)
# f(1) = x1
# f(2) = max(x2, x1)
# f(3) = max(x3 + s(2) - f(2), f(2))
# f(4) = max(x4 + s(3) - f(3), f(3))
