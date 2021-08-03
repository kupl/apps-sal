a, b, c = map(int, input().split())
print('NYoe s'[a + b == c or a + c == b or a == b + c::2])
