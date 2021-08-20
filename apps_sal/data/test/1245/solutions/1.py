n = int(input())
x = []
for i in range(n):
    x.append(list(map(int, input().split(' '))))
curr = -1
stack = []
stackelse = []
ok = 0
seq = ''
pos = 0
while pos < 2 * n:
    if stack == []:
        if ok >= n:
            print('IMPOSSIBLE')
            quit()
        stack.append(pos)
        stackelse.append(x[ok])
        ok += 1
        seq += '('
    elif stackelse[-1][0] <= pos - stack[-1] <= stackelse[-1][1]:
        stack.pop()
        stackelse.pop()
        seq += ')'
    else:
        if ok >= n:
            print('IMPOSSIBLE')
            quit()
        stack.append(pos)
        stackelse.append(x[ok])
        seq += '('
        ok += 1
    pos += 1
print(seq)
