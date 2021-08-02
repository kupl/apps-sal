a, b = list(map(int, input().split()))

add = a + b
sub = a - b
multi = a * b

print((max(add, sub, multi)))
