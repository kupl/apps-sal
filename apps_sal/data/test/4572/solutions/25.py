s = input()
al = "abcdefghijklmnopqrstuvwxyz"
for i in al:
    if i not in s:
        print(i)
        break
else:
    print("None")
