n, a, b = list(map(int, input().split()))
s = list(map(len, input().split('*')))
a_, b_ = a, b

for i in s:
    x, y = i // 2, i // 2 + i % 2
    if a > b:
        a -= y
        b -= x
    else:
        a -= x
        b -= y

print((a_ - max(0, a)) + (b_ - max(0, b)))

