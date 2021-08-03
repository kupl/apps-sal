from sys import setrecursionlimit
setrecursionlimit(200000)


class data:
    def __init__(self, a):
        self.data = a

    def qsort(self, l, r, reverse):
        if l >= r:
            return None
        ind = l
        i = l
        j = r
        key = self.data[l]
        while i < j:
            if reverse == 1:
                while (self.data[j] >= key) & (j >= l):
                    j -= 1
                while (self.data[i] < key) & (i <= r):
                    i += 1
                    ind = i - 1
                if i < j:
                    ind += 1
                    t = self.data[i]
                    self.data[i] = self.data[j]
                    self.data[j] = t
            else:
                while (self.data[j] <= key) & (j >= l):
                    j -= 1
                    ind = j + 1
                while (self.data[i] > key) & (i <= r):
                    i += 1
                if i < j:
                    ind -= 1
                    t = self.data[i]
                    self.data[i] = self.data[j]
                    self.data[j] = t
        self.qsort(l, ind, reverse)
        self.qsort(ind + 1, r, reverse)


n, m = [int(i) for i in input().split()]
a = data([int(i) for i in input().split()])
t = [None] * m
r = [None] * m
for i in range(m):
    t[i], r[i] = [int(j) for j in input().split()]
Sortlist = []
Sortcount = 0
M = 0
for i in range(m - 1, -1, -1):
    if r[i] > M:
        Sortlist.append([r[i], t[i]])
        Sortcount += 1
        M = r[i]
# a.qsort(0,Sortlist[-1][0]-1,1)
S = sorted(a.data[0:Sortlist[-1][0]])
L = 0
R = M - 1
for i in range(M - 1, -1, -1):
    if (Sortcount > 0):
        if (i < Sortlist[Sortcount - 1][0]):
            Reverse = Sortlist[Sortcount - 1][1]
            Sortcount -= 1
    if Reverse == 1:
        a.data[i] = S[R]
        R -= 1
    else:
        a.data[i] = S[L]
        L += 1
for i in a.data[0:-1]:
    print(str(i) + " ", end="")
print(a.data[-1])
