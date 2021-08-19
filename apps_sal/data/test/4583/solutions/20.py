N = input()
n = str(N)
a = int(n[0])
b = int(n[1])
c = int(n[2])
d = int(n[3])
if a + b + c + d == 7:
    ans = str(a) + '+' + str(b) + '+' + str(c) + '+' + str(d)
elif a + b + c - d == 7:
    ans = str(a) + '+' + str(b) + '+' + str(c) + '-' + str(d)
elif a + b - c + d == 7:
    ans = str(a) + '+' + str(b) + '-' + str(c) + '+' + str(d)
elif a + b - c - d == 7:
    ans = str(a) + '+' + str(b) + '-' + str(c) + '-' + str(d)
elif a - b + c + d == 7:
    ans = str(a) + '-' + str(b) + '+' + str(c) + '+' + str(d)
elif a - b + c - d == 7:
    ans = str(a) + '-' + str(b) + '+' + str(c) + '-' + str(d)
elif a - b - c + d == 7:
    ans = str(a) + '-' + str(b) + '-' + str(c) + '+' + str(d)
elif a - b - c - d == 7:
    ans = str(a) + '-' + str(b) + '-' + str(c) + '-' + str(d)
print(ans + '=7')
