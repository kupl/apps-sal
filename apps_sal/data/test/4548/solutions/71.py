(N, M, X) = map(int, input().split())
A = list(map(int, input().split()))
l_cost = 0
g_cost = 0
for i in A:
    if i > X:
        l_cost += 1
    else:
        g_cost += 1
print(min(l_cost, g_cost))
