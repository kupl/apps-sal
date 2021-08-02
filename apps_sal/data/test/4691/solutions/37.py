res = []

n = int(input())

for i in range(n):
    r = input()
    res.append(r)

ac = res.count("AC")
wa = res.count("WA")
tle = res.count("TLE")
re = res.count("RE")

print("AC x " + str(ac))
print("WA x " + str(wa))
print("TLE x " + str(tle))
print("RE x " + str(re))
