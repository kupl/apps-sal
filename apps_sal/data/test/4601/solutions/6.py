(N, K) = list(map(int, input().split()))
H = list(map(int, input().split()))
a = 0
if K > N:
    a = K - N
for _ in range(a):
    H.append(0)
H.sort(reverse=True)
sum = 0
for i in range(K):
    H[i] = 0
for i in range(N):
    sum += H[i]
print(sum)
