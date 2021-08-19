n = input()
rep = {'1': '8', '2': '7', '3': '6', '4': '5', '5': '4', '6': '3', '7': '2', '8': '1', '9': '0', '0': '9'}
num = ''
for i in range(len(n)):
    if i == 0 and n[i] == '9':
        num = num + '9'
        continue
    if int(rep[str(n[i])]) < int(n[i]):
        num = num + rep[str(n[i])]
    else:
        num = num + n[i]
print(num)
