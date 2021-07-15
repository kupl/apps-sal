a = input()
dic = {}
for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for i in dic:
    if dic[i] % 2 != 0:
        print("No")
        return
print("Yes")
