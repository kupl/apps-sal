A = int(input())
B = int(input())
C = int(input())
X = int(input())
count = 0

for i in range(A + 1):
    for j in range(B + 1):
        for k in range(C + 1):
            sum = 500 * int(i) + 100 * int(j) + 50 * int(k)
            if sum == X:
                count += 1

print(count)
