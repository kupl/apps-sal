inp = int(input())
minlchess = 0
minrchess = 10000000000
for i in range(inp):
    s = list(map(int, input().split()))
    leftchess = s[0]
    rightchess = s[1]
    if leftchess > minlchess:
        minlchess = leftchess
    if rightchess < minrchess:
        minrchess = rightchess
inp = int(input())
minlprog = 0
minrprog = 10000000000
for i in range(inp):
    s = list(map(int, input().split()))
    leftprog = s[0]
    rightprog = s[1]
    if leftprog > minlprog:
        minlprog = leftprog
    if rightprog < minrprog:
        minrprog = rightprog
dif1 = minlprog - minrchess
dif2 = minlchess - minrprog
if dif1 > dif2:
    if dif1 > 0:
        print(dif1)
    else:
        print('0')
elif dif2 > 0:
    print(dif2)
else:
    print('0')
