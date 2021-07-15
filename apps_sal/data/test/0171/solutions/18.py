S = input()
a = len(S) >= 5
b, c, d = 0, 0, 0
for i in S:
    if 'A' <= i <= 'Z':
        b = 1
    if 'a' <= i <= 'z':
        c = 1
    if '0' <= i <= '9':
        d = 1
if a + b + c + d == 4:
    print("Correct")
else:
    print("Too weak")

