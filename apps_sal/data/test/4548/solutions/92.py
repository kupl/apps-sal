(N, M, X) = map(int, input().split())
A = list(map(int, input().split()))
cost_0 = 0
cost_last = 0
for n in A:
    if n > X:
        cost_last += 1
    elif n < X:
        cost_0 += 1
if cost_0 >= cost_last:
    print(cost_last)
elif cost_0 < cost_last:
    print(cost_0)
