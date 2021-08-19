n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a = sorted(a)
hoge = 0
foo = 0
ans = 0
for i in range(n):
    if i == 0:
        foo = a[i]
        hoge = 1
    elif i == n - 1:
        if foo != a[i]:
            if hoge == 1:
                ans += 1
            ans += 1
        elif hoge == 0:
            ans += 1
    elif foo == a[i]:
        hoge = 1 - hoge
    else:
        if hoge == 1:
            ans += 1
        foo = a[i]
        hoge = 1
print(ans)
