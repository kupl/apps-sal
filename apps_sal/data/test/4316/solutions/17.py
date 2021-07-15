s = input()

a = s[0]
b = s[1]
c = s[2]
d = s[3]

if ((a == b and c == d) and a != c
    or (a == c and b == d) and a !=b
    or (a == d and b == c) and a != b):

    print("Yes")

else:
    print("No")

