n = input()
binary = []
for i in n:
    if i == '4':
        binary.append(0)
    else:
        binary.append(1)
binary.reverse()
ans = 0
for i in range(len(binary)):
    ans +=  2 ** i * (binary[i] + 1)
print (ans)
