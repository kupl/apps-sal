case=True

for i in range(8):
    s=input()
    if(s!="WBWBWBWB" and s!="BWBWBWBW"):
        case=False
if(case):
    print("YES")
else:
    print("NO")

