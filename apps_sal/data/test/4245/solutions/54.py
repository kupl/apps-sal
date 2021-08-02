A, B = map(int, input().split())
num = 1
for i in range(20):
    if i != 0:
        num += (A - 1)
    if num >= B:
        print(i)
        break
