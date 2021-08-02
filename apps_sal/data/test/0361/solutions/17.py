from fnmatch import fnmatch, fnmatchcase
pat = ["*CODEFORCES", "C*ODEFORCES", "CO*DEFORCES", "COD*EFORCES", "CODE*FORCES", "CODEF*ORCES", "CODEFO*RCES", "CODEFOR*CES", "CODEFORC*ES", "CODEFORCE*S", "CODEFORCES*"]
name = input()
ok = 0
for s in pat:
    if fnmatch(name, s):
        print("YES")
        ok = 1
        break
if ok == 0:
    print("NO")
