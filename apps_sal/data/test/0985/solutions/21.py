n = int(input())

pos = {}
neg = {}

for _ in range(n):
    x, y = list(map(int, input().split()))
    if x-y not in pos:
        pos[x-y] = 0
    if x+y not in neg:
        neg[x+y] = 0

    pos[x-y] += 1
    neg[x+y] += 1

ret = 0

for _, cnt in list(pos.items()):
    ret += cnt*(cnt-1)/2

for _, cnt in list(neg.items()):
    ret += cnt*(cnt-1)/2

print(int(ret))

