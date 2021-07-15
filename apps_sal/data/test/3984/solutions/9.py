s = input()
win1 = "Ann"
win2 = "Mike"
alth = "abcdefghijklmnopqrstuvwxyz"
num = alth.find(s[0])
for i in s:
    num2 = alth.find(i)
    if num < num2:
        print(win1)
    else:
        print(win2)
    num = min(num,num2)
