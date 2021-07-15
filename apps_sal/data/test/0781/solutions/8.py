proper = True
for i in range(8):
    raw = input()
    if raw != "WBWBWBWB" and raw != "BWBWBWBW":
        proper = False
if proper:
    print("YES")
else:
    print("NO")

