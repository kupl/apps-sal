import itertools
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

q = list(itertools.permutations(range(1, n + 1)))
ans = 0
for i in range(len(q)):
    cnt_1 = 0
    cnt_2 = 0
    if ans == 2:
        break
    for j in range(n):
        if a[j] == q[i][j]:
            cnt_1 += 1
        if b[j] == q[i][j]:
            cnt_2 += 1
    if cnt_1 == n:
        c = i + 1
        ans += 1
    if cnt_2 == n:
        d = i + 1
        ans += 1
print(abs(c - d))
