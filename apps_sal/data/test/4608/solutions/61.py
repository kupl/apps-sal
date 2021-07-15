N = int(input())
a = [0,]
for i in range(N):
    a.append(int(input()))
idx = 1
for i in range(1,N+1):
    idx = a[idx]
    if idx == 2:
        print(i)
        return
print(-1)
