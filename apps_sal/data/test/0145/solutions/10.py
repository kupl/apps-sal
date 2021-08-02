s = input()
b = {s[i] for i in range(len(s))}
if(len(b) % 2 == 0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
