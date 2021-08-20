(A, B) = map(int, input().split())
result = -1
for i in range(10 ** 3 + 1):
    if int(i * 0.08) == A:
        if int(i * 0.1) == B:
            result = i
            break
print(result)
