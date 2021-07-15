N = int(input())
AC = 0
WA = 0
TLE = 0
RE = 0
for i in range (N):
    S = input()
    if S == "AC":
        AC += 1
    elif S ==  "WA": 
        WA += 1
    elif S == "TLE":
        TLE += 1
    elif S ==  "RE":
        RE += 1
print("AC x ",AC)
print("WA x ",WA)
print("TLE x ",TLE)
print("RE x ",RE)
