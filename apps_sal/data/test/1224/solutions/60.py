n = int(input())
for i in range(1, 30):
    for j in range(1, 60):
        if 3**j + 5**i == n:
            print(j, i)
            return
print(-1)
