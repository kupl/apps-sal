(a, b) = map(int, input().split())
for i in range(25):
    if b <= a + (a - 1) * (i - 1):
        print(i)
        break
