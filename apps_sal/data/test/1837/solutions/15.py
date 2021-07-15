n = int(input())
a = list(map(int, input().split()))
ans = 0
b = True
for i in range(n):
    if a[i] == i:
        ans += 1
    elif a[a[i]] == i and b:
        ans += 2
        b = False
if b and ans < n:
    ans += 1
print(ans)
