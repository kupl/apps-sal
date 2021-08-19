(A, B) = map(int, input().split())
ca = [A // 2 % 2]
i = 2
while i <= A:
    i *= 2
    x = A % i
    ca.append((2 * x > i) * (x % 2))
B += 1
cb = [B // 2 % 2]
i = 2
while i <= B:
    i *= 2
    x = B % i
    cb.append((2 * x > i) * (x % 2))
ca += [0] * 99
cab = [a ^ b for (a, b) in zip(ca, cb)]
print(sum((cab[i] * 2 ** i for i in range(len(cab)))))
