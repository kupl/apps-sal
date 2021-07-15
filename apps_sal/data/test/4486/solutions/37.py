s = input()

N = len(s)
result = []

for i in range(0, N):
    if i == 0 or i % 2 == 0:
        result.append(s[i])

s = ''
N = len(result)

for i in range(0, N):
    s += result[i]

print(s)
