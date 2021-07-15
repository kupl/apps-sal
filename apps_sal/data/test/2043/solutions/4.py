s = input().rstrip()
line = input().rstrip()
i = 0
il = 0
while i != len(s) and il < len(line):
    if s[i] == line[il]:
        i += 1
    il += 1
x = il - 1
i = len(s) - 1
il = len(line) - 1
while i >= 0 and il >= 0:
    if s[i] == line[il]:
        i -= 1
    il -= 1
y = il + 1
if y - x > 0:
    print(y - x)
else:
    print(0)
