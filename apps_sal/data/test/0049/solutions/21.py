k = int(input())
n = 1
for i in range(1, 20):
    if k < n + 9 * 10 ** (i - 1) * i:
        print(str(10 ** (i - 1) + (k - n) // i)[(k - n) % i])
        break
    n += 9 * 10 ** (i - 1) * i
