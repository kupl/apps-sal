n = int(input())
ans = 0
curr = 0
l = list(map(int, input().split()))
for i in range(2 * n):
    if l[i % n] == 1:
        curr += 1
    else:
        curr = 0
    ans = max(ans, curr)
print(ans)
