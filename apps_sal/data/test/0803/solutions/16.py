n = int(input())
positions = list(input())
needed = n // 2
standing = 0
for i in range(n):
    if positions[i] == 'X':
        standing += 1
print(abs(needed - standing))
i = 0
while(needed > standing):
    if positions[i] == 'x':
        positions[i] = 'X'
        standing += 1
    i += 1
i = 0
while(needed < standing):
    if positions[i] == 'X':
        positions[i] = 'x'
        needed += 1
    i += 1
print(''.join(positions))
