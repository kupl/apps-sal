(n, m) = map(int, input().split())
A = list(map(int, input().split()))
bc = [list(map(int, input().split())) for _ in range(m)]
bc = sorted(bc, key=lambda x: -x[1])
sub = []
for i in range(m):
    sub += [bc[i][1]] * bc[i][0]
    if len(sub) > n:
        break
A += sub
print(sum(sorted(A, reverse=True)[:n]))
