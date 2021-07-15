s = list(input())

mylist = []
for i in range(len(s) - 2):
    number = abs(753 - int(s[i] + s[i + 1] + s[i + 2]))
    mylist.append(number)

print(min(mylist))
