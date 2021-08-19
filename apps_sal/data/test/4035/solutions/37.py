(a, b) = map(int, input().split())
for i in range(20000):
    if int(i * 8 / 100) == a and int(i * 10 / 100) == b:
        print(i)
        break
else:
    print(-1)
