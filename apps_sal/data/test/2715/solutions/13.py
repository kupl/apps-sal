K = int(input())
print(50)
A = []
for i in range(50):
    a = K % 50
    b = K // 50
    d = i + b
    if i < a:
        d += 50 - a + 1
    else:
        d -= a
    A.append(d)
print(*A)
