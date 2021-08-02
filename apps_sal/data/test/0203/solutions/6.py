n = int(input())
s = list(input())
curr_d = 0
curr_r = 0
ost_d = s.count("D")
ost_r = s.count("R")
while True:
    for i in range(len(s)):
        if s[i] == "D":
            if curr_d > 0:
                s[i] = "N"
                ost_d -= 1
                curr_d -= 1
            else:
                curr_r += 1
        if s[i] == "R":
            if curr_r > 0:
                s[i] = "N"
                ost_r -= 1
                curr_r -= 1
            else:
                curr_d += 1
    if ost_d == 0 or ost_r == 0:
        break
if ost_d == 0:
    print("R")
else:
    print("D")
