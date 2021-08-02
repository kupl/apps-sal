x = int(input())

sum = 0
for i in range(1, 100000):
    sum += i
    if sum >= x:
        print(i)
        break
