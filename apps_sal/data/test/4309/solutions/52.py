N = int(input())
count = 0
for i in range(1, 10):
    if (N - 1) // int(str(i) * 3) >= 1:
        count = i
print((str(count + 1) * 3))
