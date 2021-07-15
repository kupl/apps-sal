import sys


inputs = []
for input in sys.stdin:
    inputs.append(input.replace("\n", ""))

AC = 0
WA = 0
TLE = 0
RE = 0

for index, input in enumerate(inputs, 1):
    if input == "AC":
        AC += 1
    if input == "WA":
        WA += 1
    if input == "TLE":
        TLE += 1
    if input == "RE":
        RE += 1

print(("AC x " + str(AC) + "\nWA x " + str(WA) + "\nTLE x " + str(TLE) + "\nRE x " + str(RE)))

