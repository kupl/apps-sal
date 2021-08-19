n = input()
for i in range(len(n)):
    if n[i] == '1':
        n = n[:i] + '9' + n[i + 1:]
    else:
        n = n[:i] + '1' + n[i + 1:]
print(int(n))
