def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


n = ii()
a = li()
b = li()
done = set()
j = 0
ans = []
for i in range(n):
    if b[i] in done:
        ans.append(0)
    else:
        c = 0
        while a[j] != b[i]:
            done.add(a[j])
            j += 1
            c += 1
        done.add(a[j])
        j += 1
        ans.append(c + 1)
print(*ans)
