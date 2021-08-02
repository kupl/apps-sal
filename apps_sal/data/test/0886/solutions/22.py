n = input()
flag = False
last = int(n[-1])
for i in range(len(n)):
    if int(n[i]) % 2 == 0:
        if last > int(n[i]):
            flag = True
            print(n[:i] + str(last) + n[i + 1:-1] + n[i])
            break
if flag is False:
    for i in range(len(n) - 1, -1, -1):
        if int(n[i]) % 2 == 0:
            flag = True
            print(n[:i] + str(last) + n[i + 1:-1] + n[i])
            break
if flag == False:
    print(-1)
