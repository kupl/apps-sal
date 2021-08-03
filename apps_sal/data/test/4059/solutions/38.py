N = int(input())
count = 0

for A in range(1, N - 1):
    B = (N - 1) // A
    count += B

print(count + 1)
