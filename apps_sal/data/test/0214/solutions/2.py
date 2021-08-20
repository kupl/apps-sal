first = input()
second = input()
adad = list()
for i in range(len(first)):
    num = 0
    if first[i] == '0':
        num += 1
    if second[i] == '0':
        num += 1
    adad.append(num)
cnt = 0
last_fill = -1
for i in range(1, len(adad)):
    if adad[i] + adad[i - 1] == 3:
        cnt += 1
        adad[i] = adad[i - 1] = 0
    elif adad[i] + adad[i - 1] == 4:
        cnt += 1
        adad[i] = 1
        adad[i - 1] = 0
print(cnt)
