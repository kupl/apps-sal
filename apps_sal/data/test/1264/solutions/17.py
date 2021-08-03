n = int(input())
vec = list(map(int, input().split(' ')))
s = [0]
cnt = 0
ans = 0
for x in vec:
    s.append(x + s[-1])
    if x == 1:
        cnt = cnt + 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        one = s[i] - s[j - 1]
        tot = i - j + 1
        ans = max(ans, cnt - one + tot - one)
print(ans)
