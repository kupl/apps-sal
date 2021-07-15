n = int(input())
a = list(map(int, input().split()))
ans = -1
s = sum(a)
m = int(input())
for _ in range(m):
    l, r = list(map(int, input().split()))
    if ans == -1:
        if l <= s <= r:
            ans = s
        elif s < l:
            ans = l

print(ans)

