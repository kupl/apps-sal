n = int(input())
minn = 101
ans = 0
for i in range(n):
    (a, p) = input().split()
    a = int(a)
    p = int(p)
    if p < minn:
        minn = p
    ans += minn * a
print(ans)
