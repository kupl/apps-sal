n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))

A, B = 0, 0
for i in range(2 * n):
    if i % 2 == 0:
        if not b or a and a[-1] >= b[-1]:
            A += a[-1]
            del a[-1]
        else:
            del b[-1]
    else:
        if not a or b and b[-1] >= a[-1]:
            B += b[-1]
            del b[-1]
        else:
            del a[-1]

print(A - B)

