n = int(input())
a = [int(v) for v in input().split()]

pos, neg, zero = 0, 0, 0
for v in a:
    if v > 0:
        pos += 1
    elif v < 0:
        neg += 1
    else:
        zero += 1

if pos >= n / 2:
    print(1)
elif neg >= n / 2:
    print(-1)
else:
    print(0)
