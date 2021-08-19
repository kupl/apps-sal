(a, b) = map(int, input().split())
z = 'No'
for i in range(1, 4):
    if a * b * i % 2 == 1:
        z = 'Yes'
print(z)
