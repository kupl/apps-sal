N = int(input())
counter = {}
total = 0
for x in input().split():
    x = int(x)
    total += x
    if not x in counter:
        counter[x] = 1
    else:
        counter[x] += 1
Q = int(input())
for _ in range(Q):
    B, C = list(map(int, input().split()))
    if not B in counter:
        print(total)
        continue
    num = counter[B]
    if C in counter:
        counter[C] += num
    else:
        counter[C] = num
    total = total - num * B + num * C
    print(total)
    del counter[B]
