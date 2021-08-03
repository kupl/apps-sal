n, m, v = int(input()), int(input()), 0
for i, c in enumerate(sorted((int(input()) for i in range(n)), reverse=True)):
    v += c
    if v >= m:
        print(i + 1)
        break
