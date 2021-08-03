def readln(): return list(map(int, input().rstrip().split()))


n, x = readln()
data = list(readln())
data.sort()
count = 0
pad = 0
for i in data:
    if i < x:
        count += 1
    if i == x:
        pad = 1
print(x + pad - count)
