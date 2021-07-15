N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))
now = 99999
ans = 0
for i in range(N):
  tem = T - H[i] * 0.006
  if abs(tem - A ) < now:
    now = abs(tem - A)
    ans = i+1
print(ans)
