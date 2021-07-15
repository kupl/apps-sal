n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def yes(t):
    nonlocal n, a, b
    if len(t) < n:
        return False
    for i in range(n - 1):
        if t[i]|t[i + 1] == a[i] and t[i]&t[i + 1] == b[i]:
            continue
        else:
            return False
    return True

ans = []
for i in range(4):
    x = [i]
    for j in range(n - 1):
        for k in range(4):
            if x[-1]|k == a[j] and x[-1]&k == b[j]:
                x.append(k)
                break
    if yes(x):
        ans = x
if ans:
    print('YES')
    print(*ans)
else:
    print('NO')
