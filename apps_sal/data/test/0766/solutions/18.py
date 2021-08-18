si = [e for e in input()]
test = len(set(si))
if test > 4 or test == 1:
    print("No")
elif test == 2:
    si.sort()
    if si.count(si[0]) == 1 or si.count(si[-1]) == 1:
        print("No")
    else:
        print("Yes")
elif test == 3:
    si.sort()
    if len(si) == 3:
        print("No")
    else:
        print("Yes")
else:
    print("Yes")
