x = list(map(int, input().split()))
for i in range(5):
    if x[i] != i + 1:
        print(i + 1)
