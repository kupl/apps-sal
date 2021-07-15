n = int(input())
mas = list(map(int, input().split()))
s = sum(mas)
sc = 0
for i in range(len(mas)):
    sc += mas[i]
    if sc >= s/2:
        print(i+1)
        break

