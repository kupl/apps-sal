ls = list(map(int, input().split()))
for i in range(5):
    if ls[i] == 0:
        print(i + 1)
        break
