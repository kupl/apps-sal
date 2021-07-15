N = int(input())
T, A = list(map(int, input().split()))
H = list(map(int, input().split()))

index = 0
ans = 10**10
for i in range(N):
  tmp = T - 0.006*H[i]
  if ans > abs(A-tmp):
    ans = abs(A-tmp)
    index = i+1
print(index)

