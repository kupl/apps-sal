N = int(input())
for i in range(1,54):
    for j in range(1,36):
        if 3**i + 5**j == N:
            print(str(i) + " " + str(j))
            return
print(-1)
