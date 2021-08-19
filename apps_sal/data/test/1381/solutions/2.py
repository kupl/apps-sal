(k, n, s, p) = map(int, input().split())
person = (n - 1) // s + 1
al = person * k
pack = (al - 1) // p + 1
print(pack)
