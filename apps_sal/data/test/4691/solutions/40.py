ac = 0
wa = 0
tle = 0
re = 0
for i in range(int(input())):
    word = input()
    if word == "AC":
        ac += 1
    elif word == "WA":
        wa += 1
    elif word == "TLE":
        tle += 1
    elif word == "RE":
        re += 1
        
print("AC x " + str(ac))
print("WA x " + str(wa))
print("TLE x " + str(tle))
print("RE x " + str(re))
