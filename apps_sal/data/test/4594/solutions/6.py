N = int(input())
z = []
for num in range(101):
    z.append(0)
counter = 0
while counter < N:
    d = int(input())
    z[d] = 1
    counter += 1
result = sum(z)
print(result)
