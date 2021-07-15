N = int(input())
A = list(map(int,input().split()))
a = []
for i in range(N):
  a.append(A[i]-(i+1))
a.sort()
ave = a[N//2-1]
cnt1 = 0
cnt2 = 0
for i in range(N):
  cnt1 += abs(a[i]-ave)
for i in range(N):
  cnt2 += abs(a[i]-a[N//2])
print((min(cnt1,cnt2)))

