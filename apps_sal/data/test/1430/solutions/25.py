(n, k) = map(int, input().split())
s = input()
num = []
temp = 0
count = 0
flag = True
while temp < len(s):
    if flag == True:
        if s[temp] == '1':
            count += 1
            temp += 1
        else:
            num.append(count)
            count = 1
            temp += 1
            flag = False
    elif s[temp] == '0':
        count += 1
        temp += 1
    else:
        num.append(count)
        count = 1
        temp += 1
        flag = True
num.append(count)
num2 = [sum(num[:min(2 * k + 1, len(num))])]
temp = min(2 * k + 1, len(num))
temp2 = 0
while temp < len(num):
    temp3 = num2[-1] - num[temp2] - num[temp2 + 1] + num[temp]
    if temp + 1 < len(num):
        temp3 += num[temp + 1]
    temp += 2
    temp2 += 2
    num2.append(temp3)
print(max(num2))
