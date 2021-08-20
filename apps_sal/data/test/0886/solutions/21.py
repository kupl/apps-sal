n = input()
max = -1
temp = '-1'
for i in range(len(n)):
    if int(n[i]) % 2 == 0 and int(n[i]) < int(n[-1]):
        temp = n[0:i] + n[-1] + n[i + 1:len(n) - 1] + n[i]
        break
if temp == '-1':
    for i in range(len(n) - 2, -1, -1):
        if int(n[i]) % 2 == 0:
            temp = n[0:i] + n[-1] + n[i + 1:len(n) - 1] + n[i]
            break
print(temp)
