(a, b, x) = map(int, input().split())
st = -(-a // x)
ed = b // x
print(ed - st + 1)
