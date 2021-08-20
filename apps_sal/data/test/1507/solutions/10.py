(n, k) = list(map(int, input().split()))
s = list(input())
op = [n for _ in range(26)]
cl = [-1 for _ in range(26)]
for i in range(n):
    j = ord(s[i]) - ord('A')
    op[j] = min(op[j], i)
    cl[j] = max(cl[j], i)
cnt = [0 for _ in range(2 * n + 1)]
for i in range(26):
    if op[i] < n:
        cnt[op[i] * 2 + 1] += 1
    if -1 < cl[i]:
        cnt[cl[i] * 2 + 2] -= 1
for i in range(1, 2 * n + 1):
    cnt[i] += cnt[i - 1]
if k < max(cnt):
    print('YES')
else:
    print('NO')
