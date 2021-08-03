a = {'3': '3', '4': '6', '6': '4', '5': '9', '9': '5', '7': '7', '8': '0', '0': '8', '1': 'x', '2': 'x'}
s = input()
f = 1
for i in range(len(s)):
    if s[i] != a[s[len(s) - i - 1]]:
        f = 0
if f:
    print("Yes")
else:
    print("No")
