def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


n = ii()
s = input().strip()
i = 0
while i < n - 1:
    if ord(s[i]) > ord(s[i + 1]):
        break
    i += 1
ans = s[:i] + s[i + 1:]
print(ans)
