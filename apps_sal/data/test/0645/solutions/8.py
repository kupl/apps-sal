s = input()
k = 'aeiou13579'
c = 0
for char in s:
    if char in k:
        c += 1
print(c)
