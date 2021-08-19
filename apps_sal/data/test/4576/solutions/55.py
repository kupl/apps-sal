A = input()
B = input()
C = input()
X = input()
A = int(A)
B = int(B)
C = int(C)
X = int(X)
count = 0
for a in range(A + 1):
    for b in range(B + 1):
        for c in range(C + 1):
            x = X - (500 * a + 100 * b + 50 * c)
            if x == 0:
                count = count + 1
print(count)
