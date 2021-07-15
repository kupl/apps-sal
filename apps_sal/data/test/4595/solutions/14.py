s = list(input())

for i,j in enumerate(s):
    if j == 'A':
        a = i
        break
for i,j in enumerate(s):
    if j == 'Z':
        z = i
print(z-a+1)
