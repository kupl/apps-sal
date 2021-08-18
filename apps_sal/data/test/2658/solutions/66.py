
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
A = [a - 1 for a in A]

town = [-1] * N

move = 0
now = 0
while move < K:
    town[now] = move
    now = A[now]
    move += 1
    if town[now] != -1:
        break

cnt = (K - move) % (move - town[now])

for i in range(cnt):
    now = A[now]

print((now + 1))
