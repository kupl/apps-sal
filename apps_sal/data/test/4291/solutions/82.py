(n, q) = map(int, input().split())
s = list(map(str, input()))
arr = [list(map(int, input().split())) for j in range(q)]
result = [0]
cnt = 0
for i in range(1, len(s)):
    if s[i - 1] + s[i] == 'AC':
        cnt += 1
        result.append(cnt)
    elif s[i - 1] + s[i] != 'AC':
        result.append(cnt)
for (a, b) in arr:
    print(result[b - 1] - result[a - 1])
