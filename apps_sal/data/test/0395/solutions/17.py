a = [int(x) for x in input().split()]

sumA = 0
for i in range(6):
    sumA += a[i]

isPossible = False

for i in range(4):
    for j in range(i + 1, 5):
        for k in range(j + 1, 6):
            sumB = a[i] + a[j] + a[k]

            if sumB * 2 == sumA:
                isPossible = True

if isPossible:
    print("YES")
else:
    print("NO")
