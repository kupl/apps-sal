s = []
length = [0 for i in range(4)]
for i in range(4):
    s.append(input()[2:])
    length[i] = len(s[i])
var = []
for i in range(4):
    if length[i] >= 2 * max(length[:i] + length[i + 1:]) or length[i] <= min(length[:i] + length[i + 1:]) // 2:
        var.append(i)
if len(var) == 1:
    print(chr(ord('A') + var[0]))
else:
    print('C')
