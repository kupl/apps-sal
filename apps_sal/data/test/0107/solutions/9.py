instr = input()
firstone = instr.find("1")
if firstone == -1:
    print("no")
else:
    if instr[firstone + 1:].count("0") >= 6:
        print("yes")
    else:
        print("no")
