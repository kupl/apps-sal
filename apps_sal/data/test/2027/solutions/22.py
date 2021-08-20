input()
a = list(map(int, input().split()))
diff_sum = 0
b = []
for (i, ai) in enumerate(a[::-1]):
    bi = ai - (1 if i % 2 == 0 else -1) * diff_sum
    diff_sum += (1 if i % 2 == 0 else -1) * bi
    b.append(bi)
print(' '.join(map(str, reversed(b))))
