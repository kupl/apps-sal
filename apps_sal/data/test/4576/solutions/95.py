(A, B, C, X) = [int(input()) for i in range(4)]
ways = 0

max_a = int(X / 500)
if A < max_a:
    max_a = A
for a in reversed(list(range(max_a + 1))):
    max_b = int((X - 500 * a) / 100)
    if B < max_b:
        max_b = B
    for b in reversed(list(range(max_b + 1))):
        c = int((X - 500 * a - 100 * b) / 50)
        if c > C:
            break
        ways += 1
print(('%d' % ways))
