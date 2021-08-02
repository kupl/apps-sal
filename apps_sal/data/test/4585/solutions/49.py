X = int(input())
i = 0

while i <= X:
    c = (i * (i + 1)) / 2
    if c >= X:
        print(i)
        break
    i += 1
