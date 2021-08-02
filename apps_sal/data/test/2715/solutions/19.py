K = int(input())
q, r = K // 50, K % 50
a = [50 + q for i in range(r)] + [49 + q - r for j in range(50 - r)]

print((50))
print((' '.join(map(str, a))))
