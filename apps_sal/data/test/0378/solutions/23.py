(k, r) = map(int, input().split())
for j in range(1, 11):
    if j * k % 10 == 0 or j * k % 10 == r:
        print(j)
        break
