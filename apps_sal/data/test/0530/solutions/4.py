n = input()
s = input()
t = input()

fir = 0
sec = 0
same = 0
for (l, r) in zip(s, t):
    if l == '1':
        fir += 1
        if r == '1':
            same += 1
            sec += 1
    elif r == '1':
        sec += 1

if same % 2 != 0:
    fir += 1

if fir > sec:  # or (sec - fir <= 1 and same % 2 != 0):
    print("First")
elif sec > fir + 1:  # or (sec - fir <= 1 and same % 2 == 0):
    print("Second")
else:
    print("Draw")
