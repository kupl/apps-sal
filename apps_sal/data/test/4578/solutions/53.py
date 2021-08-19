(N, X) = map(int, input().split())
(m, min_value, count, ans) = ([], 1000, 0, N)
for i in range(N):
    m.append(int(input()))
    min_value = min(min_value, m[i])
    count += m[i]
while True:
    if X - count >= min_value:
        count += min_value
        ans += 1
    else:
        break
print(ans)
