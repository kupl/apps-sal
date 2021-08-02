completed = {}

alice = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
bob = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]


def simulate(i):

    nonlocal s, a, b, l, m, completed
    if(str(a) + " " + str(b) in completed):
        return
    s.append(alice[a - 1][b - 1])
    temp1 = a
    temp2 = b
    completed[str(a) + " " + str(b)] = i
    a = l[temp1 - 1][temp2 - 1]
    b = m[temp1 - 1][temp2 - 1]
    simulate(i + 1)


k, a, b = list(map(int, input().split()))
l = []
for i in range(3):
    l.append(list(map(int, input().split())))
m = []
for i in range(3):
    m.append(list(map(int, input().split())))

s = []
ali = 0
bo = 0
simulate(0)
for i in range(completed[str(a) + " " + str(b)]):
    if(k == 0):
        break
    k -= 1
    if(s[i] == 1):
        ali += 1
    elif(s[i] == -1):
        bo += 1
s = s[completed[str(a) + " " + str(b)]:]
awins = s.count(1)
bwins = s.count(-1)
mul = k // len(s)
rem = k % len(s)
ali += mul * awins
bo += mul * bwins
for i in range(rem):
    if(s[i] == 1):
        ali += 1
    elif(s[i] == -1):
        bo += 1
print(ali, bo)
