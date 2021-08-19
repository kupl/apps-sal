n = int(input())
sum = 0
i = 1
while i < n:
    sum += (n - i) * i
    i += 1
print(sum + n)
