def read():
    return map(int, input().split())


(a, b, c) = read()
ans = c * 2 + (b * 2 if a == b else min(a, b) * 2 + 1)
print(ans)
