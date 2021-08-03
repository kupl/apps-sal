n = int(input()) + 1
a = sum(map(int, input().split()))
c = 0
for i in range(1, 6):
    if (a + i) % n != 1:
        c += 1

print(c)
