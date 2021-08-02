n = int(input())

s = [input() for i in range(n)]

numAC = 0
numWA = 0
numTLE = 0
numRE = 0

for i in range(len(s)):
    if s[i] == "AC":
        numAC += 1
    elif s[i] == "WA":
        numWA += 1
    elif s[i] == "TLE":
        numTLE += 1
    elif s[i] == "RE":
        numRE += 1
    else:
        continue
print("AC x {}\nWA x {}\nTLE x {}\nRE x {}".format(numAC, numWA, numTLE, numRE))
