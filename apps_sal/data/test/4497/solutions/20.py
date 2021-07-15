n = int(input())
count = [0] * n
for i in range(1, n + 1):
    num = i
    while num % 2 == 0:
        num //= 2
        count[i - 1] += 1
print(count.index(max(count)) + 1)
