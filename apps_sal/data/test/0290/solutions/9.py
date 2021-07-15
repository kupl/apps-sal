def ii():
    return int(input())
def mi():
    return list(map(int, input().split()))
def li():
    return list(mi())

n = ii()
for i in range(1, n + 1):
    if i * i > n:
        break
i -= 1
ans = 2 * i
if n - i * i == 0:
    pass
elif n - i * i <= i:
    ans += 1
else:
    ans += 2
print(ans)

