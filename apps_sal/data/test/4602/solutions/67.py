n = int(input())
k = int(input())
v = list(map(int, input().split()))
ans = 0
for i in v:
    tmp = min(i, k - i)
    ans += tmp
print(ans * 2)
