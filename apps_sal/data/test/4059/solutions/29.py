N = int(input())
count = 0
for a in range(1, N):
    g = N // a
    if N % a == 0:
        g += -1
    count += g
print(count)
