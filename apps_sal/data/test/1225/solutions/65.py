h = int(input())
for i in range(100):
    if 2**i > h:
        print(2**i - 1)
        return
