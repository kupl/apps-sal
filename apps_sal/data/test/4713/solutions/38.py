x = int(input())
s = input()
li = [0]
c = 0
for i in range(x):
    if s[i] == 'I':
        c += 1
        li.append(c)
    else:
        c -= 1
        li.append(c)
print(max(li))
