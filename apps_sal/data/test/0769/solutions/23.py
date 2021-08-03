a, b, c = list(map(int, input().split()))
store = []
cnt = 1
while cnt < 1000:
    a = a * 10
    d = a // b
    store.append(d)
    a = a % b
    cnt += 1

pos = -111
try:
    pos = store.index(c)
except ValueError:
    pos = -1

print(pos if pos == -1 else pos + 1)
