n = input()
n = list(n)
mylist = []
for i in range(len(n)):
    if n[i] == '0':
        mylist.append(2)
    elif n[i] == '1':
        mylist.append(7)
    elif n[i] == '2':
        mylist.append(2)
    elif n[i] == '3':
        mylist.append(3)
    elif n[i] == '4':
        mylist.append(3)
    elif n[i] == '5':
        mylist.append(4)
    elif n[i] == '6':
        mylist.append(2)
    elif n[i] == '7':
        mylist.append(5)
    elif n[i] == '8':
        mylist.append(1)
    elif n[i] == '9':
        mylist.append(2)
print(mylist[0] * mylist[1])
