n = int(input())
l = []
for i in range(n):
    l.append(str(input()))
print(("AC x "+str(l.count('AC'))))
print(("WA x "+str(l.count('WA'))))
print(("TLE x "+str(l.count('TLE'))))
print(("RE x "+str(l.count('RE'))))

