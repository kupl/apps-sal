d = input().split()
k = int(d[0])
r = int(d[1])
for i in range(1, 11):
    if (k * i - r) % 10 == 0 or k * i % 10 == 0:
        print(i)
        break
