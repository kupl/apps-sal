s = input()

l = len(s)
num = 0
count = 0
dic = {0: 1}
for i in range(l - 1, -1, -1):
    num = (num + int(s[i]) * pow(10, l - i - 1, 2019)) % 2019
    if num not in dic:
        dic[num] = 1
    else:
        dic[num] += 1
for ele in list(dic.values()):
    count += ele * (ele - 1) // 2
print(count)
