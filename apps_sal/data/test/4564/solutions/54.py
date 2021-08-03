s = input()
a = ""
for i in s:
    if a.find(i) == -1:
        a += i
    else:
        print("no")
        break
else:
    print("yes")
