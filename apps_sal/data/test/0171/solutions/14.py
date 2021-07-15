s = input()
if len(s) < 5:
    print("Too weak")
else:
    a = b = c = False
    for i in range(0, 26):
        if chr(ord('A') + i) in s:
            a = True
        if chr(ord('a') + i) in s:
            b = True
        if i < 10 and chr(ord('0') + i) in s:
            c = True
    if a and b and c:
        print("Correct")
    else:
        print("Too weak")
