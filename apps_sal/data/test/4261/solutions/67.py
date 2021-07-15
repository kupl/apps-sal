
a, b, c = map(int, input().split())

# 容器１の空き容量x
x = a - b

# 容器２に残る水の量y
y = c - x
if c - x >= 0:
    print(y)

if c - x <0:
    print('0')
