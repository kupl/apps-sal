n = int(input())
m = list(map(int, input().split()))
lt = m[-1]
it = len(m) - 1
ans = 1
for j in range(len(m) - 2, -1, -1):
    if j >= it - lt:
        ans += 0
    else:
        ans += 1
    if j - m[j] < it - lt:
        it = j
        lt = m[j]
print(ans)
