n = int(input())
P = list(map(int, input().split()))
li = [0]*n
cnt = 0
for i in range(n):
    if P[i]==i+1:
        li[i]=1
        cnt += 1
for i in range(n-1):
    if li[i+1] and li[i]:
        li[i+1] = 0
        li[i] = 0
        cnt -= 1
print(cnt)

