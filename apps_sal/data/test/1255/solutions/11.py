dic = {}

for i in range(int(input())):
    a = input()
    dic[a] = dic.get(a, 0) + 1

print(max(dic.values()))
