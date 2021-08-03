N = int(input())
A = sorted([int(input()) for _ in range(N)])
rets = 0
for i in range(N):
    x, y = 0, N - 1
    curr = 2 * A[i]
    while x < y:
        sums = A[x] + A[y]
        if sums < curr:
            x += 1
        elif sums > curr:
            y -= 1
        else:
            rets += 1
            break
print(rets)
