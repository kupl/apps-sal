n = int(input())
p = list(map(int, input().split()))
ps = sorted(p)
cnt = 0
for (i, j) in zip(p, ps):
    if i != j:
        cnt += 1
print('YES' if cnt <= 2 else 'NO')
