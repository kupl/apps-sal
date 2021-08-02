N = int(input())
S = ["AC", "WA", "TLE", "RE"]
a = []
ac = 0
wa = 0
tle = 0
re = 0
if N >= 1 and N <= 10**5:
    for x in range(N):
        a.append(input())
for x in a:
    if x == "AC":
        ac += 1
print("AC x ", ac)
for x in a:
    if x == "WA":
        wa += 1
print("WA x ", wa)
for x in a:
    if x == "TLE":
        tle += 1
print("TLE x ", tle)
for x in a:
    if x == "RE":
        re += 1
print("RE x ", re)
