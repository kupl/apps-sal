S = int(input())
(a, b, c) = (1, 0, 0)
for n in range(S):
    (a, b, c) = (b, c, (a + c) % (10 ** 9 + 7))
print(a)
