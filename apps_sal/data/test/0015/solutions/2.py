(a, b, c) = list(map(int, input().split()))
if c != 0:
    n = (b - a) // c
else:
    n = 0
print(['NO', 'YES'][a + n * c == b and n >= 0])
