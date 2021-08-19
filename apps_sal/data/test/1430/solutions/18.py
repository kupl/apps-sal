(N, K) = map(int, input().split())
s = str(input())
l = []
(tmp, cnt) = (s[0], 1)
for i in range(1, N):
    if s[i] == tmp:
        cnt += 1
    else:
        tmp = s[i]
        l.append(cnt)
        cnt = 1
l.append(cnt)
(start, goal) = (0, len(l))
if s[0] == '0':
    start += 1
if s[-1] == '0':
    goal -= 1
ans = sum(l[start:start + 2 * K + 1])
tmp = ans
for i in range(start, goal - 2 * K - 2, 2):
    tmp += l[i + 2 * K + 1] + l[i + 2 * K + 2] - l[i] - l[i + 1]
    ans = max(ans, tmp)
if ans < sum(l[:2 * K]):
    ans = sum(l[:2 * K])
if ans < sum(l[-2 * K:]):
    ans = sum(l[-2 * K:])
print(ans)
