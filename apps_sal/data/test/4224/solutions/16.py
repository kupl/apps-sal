input()
n = 0
for a in map(int, input().split()):
    while a % 2 == 0:
        a /= 2
        n += 1
print(n)
