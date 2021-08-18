
k = int(input())
a = 7
for i in range(k + 1):
    if a % k == 0:
        print((i + 1))
        break
    else:
        a = (a * 10 + 7) % k
else:
    print((-1))
