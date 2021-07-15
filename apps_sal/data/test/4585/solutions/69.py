x = int(input())
for i in range(1000000000):
    if x <= i*(i+1)/2:
        print(i)
        return

