x = input()
if len(x) < 10:
    print("NO")
else:
    if ((x[0:1] == "C") and (x[len(x) - 9:len(x)] == "ODEFORCES")) or ((x[0:2] == "CO") and (x[len(x) - 8:len(x)] == "DEFORCES")) or ((x[0:3] == "COD") and (x[len(x) - 7:len(x)] == "EFORCES")) or ((x[0:4] == "CODE") and (x[len(x) - 6:len(x)] == "FORCES")) or ((x[0:5] == "CODEF") and (x[len(x) - 5:len(x)] == "ORCES")) or ((x[0:6] == "CODEFO") and (x[len(x) - 4:len(x)] == "RCES")) or ((x[0:7] == "CODEFOR") and (x[len(x) - 3:len(x)] == "CES")) or ((x[0:8] == "CODEFORC") and (x[len(x) - 2:len(x)] == "ES")) or ((x[0:9] == "CODEFORCE") and (x[len(x) - 1:len(x)] == "S")) or ((x[0:10] == "CODEFORCES") or (x[len(x) - 10:len(x)] == "CODEFORCES")):
        print("YES")
    else:
        print("NO")
