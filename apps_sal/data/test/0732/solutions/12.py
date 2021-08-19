def ii():
    return int(input())


def kk():
    return map(int, input().split())


def ll():
    return list(kk())


q = []
s = set()
n = ii()
for x in range(10):
    for y in range(10):
        q.append(x)
        while q:
            q2 = []
            for item in q:
                if item > 0 and item <= n:
                    s.add(item)
                    item *= 10
                    q2.append(item + x)
                    q2.append(item + y)
            q = q2
print(len(s))
