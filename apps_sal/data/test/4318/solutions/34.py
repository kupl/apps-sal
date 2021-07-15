N = int(input())
H = list(map(int, input().split()))
count = 1
for i in range(1, N):
  k = N - i
  temp = H[k]
  del H[-1]
  if temp >= max(H):
    count += 1
print(count)
