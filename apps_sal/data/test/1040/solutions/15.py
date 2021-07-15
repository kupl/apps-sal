n = int(input())
s = input()
tmp = []
for i in s:
    tmp.append(i)
    if len(tmp) >= 3:
        if tmp[-3:] == ["f","o","x"]:
            tmp.pop()
            tmp.pop()
            tmp.pop()
        
print((len(tmp)))

