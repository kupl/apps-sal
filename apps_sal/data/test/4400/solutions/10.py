S = input()
if S.count('R') == 1:
    print(1)
elif S.count('R') == 0:
    print(0)
elif S.count('S') == 0:
    print(3)
elif S.count('RR') == 1:
    print(2)
else:
    print(1)
