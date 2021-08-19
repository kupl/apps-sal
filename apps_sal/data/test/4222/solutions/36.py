(n, k) = list(map(int, input().split()))
l1 = []
safe = []
ans = 0
for i in range(k):
    d = int(input())
    l = list(map(int, input().split()))
    safe += l
for i in range(1, n + 1):
    if i not in list(set(safe)):
        ans += 1
print(ans)
