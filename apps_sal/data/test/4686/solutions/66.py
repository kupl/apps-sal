w = input()

dic = {}
for c in w:
    if c not in dic:
        dic[c] = 1
    else:
        dic[c] += 1
        
for key in dic:
    if dic[key] % 2 != 0:
        print("No")
        return
print("Yes")

