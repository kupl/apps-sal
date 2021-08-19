def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


n = ii()
cnt = 0
ans = []
while True:
    i = 0
    while n & 1 << i:
        i += 1
    if 2 ** i > n:
        break
    j = i + 1
    while not n & 1 << j:
        j += 1
    ans.append(j)
    cnt += 1
    while j > 0:
        j -= 1
        n ^= 1 << j
    if not n + 1 & n:
        break
    n += 1
    cnt += 1
print(cnt)
print(*ans)
