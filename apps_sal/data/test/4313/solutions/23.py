n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if v[i] > c[i]:
        cnt += v[i] - c[i]
print(cnt)
