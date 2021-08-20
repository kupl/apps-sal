s = 0
n = int(input())
i = 1
while True:
    s += i
    n -= s
    if n >= 0:
        i += 1
    else:
        break
print(i - 1)
