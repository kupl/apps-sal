'''
template author-: Pyduper
'''


N = 250
n, k = map(int, input().split())

segs = [[0, 0] for _ in range(n)]
cnt = [0] * N
ans = [0] * n
for i in range(n):
    segs[i][0], segs[i][1] = map(int, input().split())
    cnt[segs[i][0]] += 1
    cnt[segs[i][1] + 1] -= 1

for i in range(N - 1):
    cnt[i + 1] += cnt[i]

for i in range(N - 1):
    while cnt[i] > k:
        pos = -1
        for p in range(n):
            if not ans[p] and segs[p][0] <= i <= segs[p][1] and (pos == -1 or segs[p][1] > segs[pos][1]):
                pos = p
        assert pos != -1

        for j in range(segs[pos][0], segs[pos][1] + 1):
            cnt[j] -= 1
        ans[pos] = 1
print(ans.count(1))
for i in range(n):
    if ans[i]:
        print(i + 1, end=" ")
print()
