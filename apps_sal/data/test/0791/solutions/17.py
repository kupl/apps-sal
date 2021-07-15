n = int(input())
ar = input()
ind = 0
s = 0
for i in ar:
    if i == '1' and ind == 0:
        s += 1
    else:
        ind = 1
if s < len(ar):
    print(s + 1)
else:
    print(len(ar))
