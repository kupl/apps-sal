nlr = input().split()
a = input().split()
b = input().split()

if (a[:int(nlr[1]) - 1] != b[:int(nlr[1]) - 1]) | (a[int(nlr[2]) + 1:] != b[int(nlr[2]) + 1:]) | (sorted(a[int(nlr[1]) - 1:int(nlr[2])]) != sorted(b[int(nlr[1]) - 1:int(nlr[2])])):
    print("LIE")
else:
    print("TRUTH")
