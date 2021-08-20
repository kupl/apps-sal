a = input()
b = input()
i = len(a) - 1
j = len(b) - 1
while a[i] == b[j]:
    i -= 1
    j -= 1
    if i < 0 or j < 0:
        break
print(i + j + 2)
