class lq(list):

    def __init__(self):
        self.value = []
        self.lenght = 0
        self.startPos = 0
        self.maxLen = 50000

    def append(self, item):
        self.value.append(item)
        self.lenght += 1

    def pop(self):
        if self.startPos < self.maxLen:
            rv = self.value[self.startPos]
            self.lenght -= 1
            self.startPos += 1
            return rv
        else:
            rv = self.value[self.startPos]
            self.lenght -= 1
            self.value[0:self.startPos + 1] = []
            self.startPos = 0
            return rv


n = int(input())
s = input()
qforD = lq()
qforR = lq()
for i in range(n):
    if s[i] == 'D':
        qforD.append(i)
    else:
        qforR.append(i)
cnt = n
while qforD.lenght > 0 and qforR.lenght > 0:
    dNum = qforD.pop()
    rNum = qforR.pop()
    if dNum < rNum:
        qforD.append(cnt)
    else:
        qforR.append(cnt)
    cnt += 1
if qforD.lenght == 0:
    print('R')
else:
    print('D')
