(a, b, c, d) = list(map(int, input().split()))
hoge = [a * c, a * d, b * c, b * d]
print(max(hoge))
