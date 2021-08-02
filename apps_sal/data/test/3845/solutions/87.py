a, b = map(int, input().split())
m = [[0 for _ in range(100)] for _ in range(100)]
# paint lower half as 1
for i in range(50, 100):
    for j in range(100):
        m[i][j] = 1
a -= 1  # 0 means black
b -= 1  # 1 means white
# paint chess board like pattern of b white dots in upper half
for i in range(0, 48, 2):
    if b == 0:
        break
    for j in range(0, 100, 2):
        m[i][j] = 1
        b -= 1
        if b == 0:
            break

# now paint a black dots in lower half
for i in range(99, 50, -2):
    if a == 0:
        break
    for j in range(0, 100, 2):
        m[i][j] = 0
        a -= 1
        if a == 0:
            break
print(100, 100)
for i in range(100):
    for j in range(100):
        if m[i][j] == 0:
            print('.', end='')
        else:
            print('#', end='')
    print()
