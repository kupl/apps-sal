(n, a, b) = map(int, input().split())
A = list(map(int, input().split()))
B = A[::-1]
cheapest = min(a, b)
cost = 0
bad = False
for i in range(n):
    if A[i] != B[i]:
        if A[i] != 2 and B[i] != 2:
            bad = True
        elif A[i] == 2:
            if B[i] == 0:
                cost += a
            else:
                cost += b
    elif A[i] == 2:
        cost += cheapest
if bad:
    print(-1)
else:
    print(cost)
