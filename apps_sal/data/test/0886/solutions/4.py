x = input()

pos = -1
last = ord(x[-1]) - 48
for i, c in enumerate(x):
    cur = ord(c) - 48
    if not cur & 0b1:
        pos = i
        if last > cur:
            print(x[:i] + x[-1] + x[i+1:-1] + x[i])
            break
else:
    if pos != -1:
        print(x[:pos] + x[-1] + x[pos + 1:-1] + x[pos])
    else:
        print(-1)

