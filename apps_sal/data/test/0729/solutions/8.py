def ii():
    return int(input())
def mi():
    return list(map(int, input().split()))
def li():
    return list(mi())

n = ii()
s = input().strip()
ans = 'NO'
for i in range(n - 1):
    if s[i] != s[i + 1]:
        ans = 'YES\n' + s[i:i + 2]
        break
print(ans)

