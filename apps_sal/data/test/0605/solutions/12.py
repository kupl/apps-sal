s = input()
s = s.split()


def m(a, b):
    return max(3 * a / 10, a - a * b / 250)


for i in range(len(s)):
    s[i] = int(s[i])
if m(s[0], s[2]) > m(s[1], s[3]):
    print("Misha")
elif m(s[0], s[2]) < m(s[1], s[3]):
    print("Vasya")
else:
    print("Tie")
