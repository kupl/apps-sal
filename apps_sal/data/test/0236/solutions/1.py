s = input()
a = s.count('o')
b = s.count('-')
if (a == 0):
    print('YES')
elif b % a == 0:
    print("YES")
else:
    print("NO")

