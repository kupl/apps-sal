(N, K) = map(int, input().split())
d = 0
A = []
okashi = [0] * N
ans = 0
for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for j in range(d):
        okashi[A[j] - 1] += 1
for num in okashi:
    if num == 0:
        ans += 1
print(ans)
