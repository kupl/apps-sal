K = int(input())
odd = 0
even = 0
for i in range(1, K + 1):
    if i % 2 == 0:
        odd += 1
    else:
        even += 1

print(odd * even)
