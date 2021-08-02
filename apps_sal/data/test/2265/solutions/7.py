a = input()
b = input()
A = [0]
Hash = 0
for i in a:
    if i == '1':
        A.append(A[-1] + 1)
    else:
        A.append(A[-1])
for i in b:
    if i == '1':
        Hash += 1
res = 0
for i in range(1, len(a) - len(b) + 2):
    if ((A[i + len(b) - 1] - A[i - 1]) % 2) == (Hash % 2):
        res += 1
print(res)
