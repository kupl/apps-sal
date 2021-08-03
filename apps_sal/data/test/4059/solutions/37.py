N = int(input())
count = 0
for i in range(1, N):
    h = (N - 1) // i
    count += h
print(count)
