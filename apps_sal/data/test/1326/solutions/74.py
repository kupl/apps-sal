N = int(input())
count = 0
for i in range(1, N + 1):
    t = N // i
    count += i * t * (t + 1) / 2
print(int(count))
