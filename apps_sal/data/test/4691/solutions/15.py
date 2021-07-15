N = int(input())
S = [input() for i in range(N)]

nac = len([s for s in S if s == "AC"])
nwa = len([s for s in S if s == "WA"])
ntle = len([s for s in S if s == "TLE"])
nre = len([s for s in S if s == "RE"])

print(("AC x " + str(nac)))
print(("WA x " + str(nwa)))
print(("TLE x " + str(ntle)))
print(("RE x " + str(nre)))

