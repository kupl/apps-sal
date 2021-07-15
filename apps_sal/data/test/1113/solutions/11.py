n = int(input())
mas = list(map(int, input().split()))
maxx = -1
f = 0
for i in range(n):
    if mas[i] > maxx:
        if mas[i] - 1 > maxx:
            print(i + 1)
            f = 1
            break
        else:
            maxx += 1
if f == 0:
    print(-1)
