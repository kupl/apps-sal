n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
cnt = 0
for i in range(k):
    cnt += l[i]
print(cnt)
