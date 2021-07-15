N, K = map(int, input().split())
H = list(map(int, input().split()))

H = sorted(H)
hp = 0
for i in range(N-K):
  hp += H[i]
print(hp)
