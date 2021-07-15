n = int(input())   
cnt = {i: 0 for i in range(1, 7)}
cnt[0] = float('inf')
f = {x: i + 1 for i, x in enumerate((4, 8, 15, 16, 23, 42))}
for e in map(int, input().split()):
    e = f[e]
    if cnt[e - 1] > 0:
        cnt[e] += 1
        cnt[e - 1] -= 1
print(n - 6 * cnt[6])
