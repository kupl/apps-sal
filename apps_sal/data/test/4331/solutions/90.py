N = input()

flag = False

for i in range(len(N)):
    if N[i] == '7':
        flag = True

print('Yes' if flag else "No")
