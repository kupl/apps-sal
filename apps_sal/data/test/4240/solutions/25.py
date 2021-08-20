s = input()
t = input()
flag = False
for i in range(1, len(s) + 1):
    if s[-i:] + s[:len(s) - i] == t:
        flag = True
        break
print('Yes' if flag else 'No')
