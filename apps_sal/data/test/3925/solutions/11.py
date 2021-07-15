s = input()
tot = len(s)
s = s + s
maxVal = 1
currVal = 1
curr = s[0]
for i in range(1, len(s)):
    if s[i] == curr:
        currVal = 1
    else:
        currVal += 1
        curr = s[i]
        if maxVal < currVal:
            maxVal = currVal
if maxVal > tot:
    maxVal = tot
print(maxVal)
