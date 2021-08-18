N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
C = list(map(int, input().split()))
K = list(map(int, input().split()))

CC = [-1] * N
Ans = [-2] * N
total_cost = 0
for _ in range(N):
    mi = float("inf")
    for i, (c, an) in enumerate(zip(C, Ans)):
        if an == -2 and mi > c:
            mi = c
            ami = i
    total_cost += mi
    Ans[ami] = CC[ami]
    k1 = K[ami]
    x1, y1 = XY[ami]
    for i, (k2, (x2, y2)) in enumerate(zip(K, XY)):
        new_cost = (k1 + k2) * (abs(x1 - x2) + abs(y1 - y2))
        if C[i] > new_cost:
            C[i] = new_cost
            CC[i] = ami
print(total_cost)
cnt = Ans.count(-1)
print(cnt)
A = []
B = []
for i, a in enumerate(Ans, 1):
    if a == -1:
        A.append(i)
    else:
        B.append((i, a + 1))
print(" ".join(map(str, A)))
print(N - cnt)
for a, b in B:
    print(a, b)
