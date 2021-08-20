def read():
    return list(map(int, input().split()))


(n, h) = read()
a = list(read())
ans = n + sum((i > h for i in a))
print(ans)
