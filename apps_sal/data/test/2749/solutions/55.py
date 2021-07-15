h, w = list(map(int, input().split()))
n = int(input())
a = list(map(int, input().split()))
ret = [[0] * w for i in range(h)]

line = []

for i, item in enumerate(a):
    line.extend([i+1] * item)

for i, item in enumerate(line):
    sho = i // w
    amari = i % w
    if sho % 2 == 0:
        ret[sho][amari] = item
    else:
        ret[sho][w-1-amari] = item

for item in ret:
    print((' '.join(map(str, item))))

