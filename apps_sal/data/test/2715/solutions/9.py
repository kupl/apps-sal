K = int(input())
N = 50
P, Q = -(-K // N), -K % N
ans = [i for i in range(P, P + N)]

for q in range(Q):
    for i in range(N):
        if i == N - 1 - q:
            ans[i] -= N
        else:
            ans[i] += 1

print(N)
print(*ans)
