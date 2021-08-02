n, m = map(int, input().split())
k = []
cnt = 0

for i in range(n):
    tmp = input().split()
    tmp.pop(0)
    k += tmp

for i in range(m):
    if k.count(str(i + 1)) == n:
        cnt += 1

print(cnt)
