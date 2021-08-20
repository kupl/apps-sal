(n, x) = map(int, input().split())
li = list(map(int, input().split()))
lis = []
sum = 0
for i in range(n):
    sum += li[i]
    lis.append(sum)
cnt = 0
for i in lis:
    if i <= x:
        cnt += 1
print(cnt + 1)
