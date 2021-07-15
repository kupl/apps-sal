n, m = map(int, input().split())
res = [set(map(int, input().split())) for _ in range(m)]
a = res[0]
has = False
for i in range(m):
    if not res[i] & a:
        b = res[i]
        has = True
if not has:
    print("YES")
    return
for x in a:
    for y in b:
        fail = False
        for _ in res:
            if x not in _ and y not in _:
                fail = True
        if not fail:
            print("YES")
            return
print("NO")
