n = int(input())

ac = 0
wa = 0
tle = 0
re = 0

for i in range(n):
    result = input()
    if result == "AC":
        ac = ac + 1
    elif result == "WA":
        wa = wa + 1
    elif result == "TLE":
        tle = tle + 1
    elif result == "RE":
        re = re + 1

print("AC x " + str(ac))
print("WA x " + str(wa))
print("TLE x " + str(tle))
print("RE x " + str(re))
