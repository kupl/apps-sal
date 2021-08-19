(n, m) = map(int, input().split())
line = [0 for i in range(m + 1)]
ans = 0
for i in range(n):
    like_list = list(map(int, input().split()))
    for j in range(like_list[0]):
        line[like_list[j + 1]] += 1
for i in range(m + 1):
    if line[i] == n:
        ans += 1
print(ans)
