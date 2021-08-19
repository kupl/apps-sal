(x, a, b) = map(int, input().split())
print([['dangerous', 'safe'][a + x >= b], 'delicious'][a >= b])
