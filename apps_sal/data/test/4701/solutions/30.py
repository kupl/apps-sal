n = int(input())
k = int(input())

cnt = 1
tmp = 0
for i in range(n):
    cnt = min(cnt*2, cnt + k)
print(cnt)
