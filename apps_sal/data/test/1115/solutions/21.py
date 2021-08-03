def R(): return list(map(int, input().split()))


input()
a = sum(R())
for i in range(int(input())):
    c, d = R()
    if c <= a <= d:
        print(a)
        return
    elif a < c:
        print(c)
        return
print(-1)
