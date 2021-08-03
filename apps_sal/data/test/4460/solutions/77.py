data = [int(x) for x in input().split(" ")]

for i in range(len(data)):
    if data[i] == 0:
        print((i + 1))
