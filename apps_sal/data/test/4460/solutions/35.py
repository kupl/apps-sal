x = input()
x = list(map(int, x.split()))
for i in range(len(x)):
    if x[i] == 0:
        print(i + 1)
