has = input()
need = input()
A, B = [0] * 26, [0] * 26
for i in has:
    A[ord(i) - 97] += 1
for i in need:
    B[ord(i) - 97] += 1
result = 0
for i in range(26):
    if not A[i] and B[i]:
        result = -1
        break
    else:
        result += min(A[i], B[i])
print(result)
