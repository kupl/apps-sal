a = int(input())
b = list(map(int, input().split()))
sumA = 0
sumB = 0
for i in range(a):
    if b[a - 1 - i] > abs(sumA - sumB):
        sumA += b[a - 1 - i]
        sumA, sumB = sumB, sumA
    else:
        sumA += b[a - 1 - i]
print(min(sumA, sumB), max(sumA, sumB))
