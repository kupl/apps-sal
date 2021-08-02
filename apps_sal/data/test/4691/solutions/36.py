count = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}
for i in range(int(input())):
    x = str(input())
    if x in count:
        count[x] += 1

print("AC x " + str(count["AC"]))
print("WA x " + str(count["WA"]))
print("TLE x " + str(count["TLE"]))
print("RE x " + str(count["RE"]))
