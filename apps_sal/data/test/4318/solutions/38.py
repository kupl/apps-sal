n = int(input())
q = list(map(int, input().split()))
m = 0
cnt = 0
for i in range(n):
    if m <= q[i]:
        cnt += 1
    m = max(q[i], m)

print(cnt)
