n = int(input())
cnt = 0
for i in range(0, n):
    (p, q) = input().split(' ')
    if int(q) - int(p) >= 2:
        cnt += 1
print(cnt)
