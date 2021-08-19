import sys
a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
(la, lb) = (len(a), len(b))
(sum, cur) = (0, 0)
for i in range(lb - la + 1):
    cur += int(b[i])
for i in range(la):
    if a[i] == '0':
        sum += cur
    else:
        sum += lb - la + 1 - cur
    if i != la - 1:
        if b[i] == '1':
            cur -= 1
        if b[lb - la + i + 1] == '1':
            cur += 1
print(sum)
