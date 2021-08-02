k = int(input())
a = 7 % k
for i in range(k + 1):
    if a == 0:
        print(i + 1)
        break
    a = (a * 10 + 7) % k
else:
    print(-1)
