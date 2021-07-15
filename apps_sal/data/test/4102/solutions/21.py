a=input()
d={"0":"8","1":"-","2":"-","3":"3","4":"6","5":"9","6":"4","7":"7","8":"0","9":"5"}
for i in range(len(a)):
    if d[a[i]]!=a[len(a)-i-1]:
        print("No")
        return
print("Yes")
