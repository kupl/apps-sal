n, a, b, c = list(map(int, input().split()))

sum = -1

for A in range(4):
    for B in range(3):
        for C in range(4):
            N = n + A + B * 2 + C * 3
            if N % 4 == 0:
                if sum == -1 or A * a + B * b + C * c < sum:
                    sum = A * a + B * b + C * c

print (sum)

