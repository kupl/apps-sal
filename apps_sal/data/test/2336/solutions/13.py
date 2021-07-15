import math
from sys import stdin, stdout
input = stdin.readline


class N:
    def __init__(self, il, ir, val, l, r):
        self.il = il
        self.ir = ir
        self.val = val
        self.l = l
        self.r = r

    def __str__(self):
        return ' il = ' + str(self.il) + ' ir = ' + str(self.ir) + ' val = ' + str(self.val)

    def get_amount(self,left,right,func):
        if self.il==left and self.ir==right:
            return self.val
        elif self.l.il<=left and self.l.ir>=right:
            return self.l.get_amount(left,right,func)
        elif self.r.il<=left and self.r.ir>=right:
            return self.r.get_amount(left,right,func)
        else:
            return func(self.l.get_amount(left,self.l.ir,func),self.r.get_amount(self.r.il,right,func))


class ST:
    def __init__(self, arr, threshold):
        t1 = []
        t2 = []
        for i, val in enumerate(arr):
            t1.append(N(i, i, int(val >= threshold), None, None))
        while len(t1) + len(t2) > 1:
            while len(t1) >= 2:
                a = t1.pop()
                b = t1.pop()
                t2.append(self.__get_next(a, b))
            if len(t1) > 0:
                t2.append(t1.pop())
            t1, t2 = t2, t1
        self.r = t1[0]

    def __get_next(self, a, b):
        if a.il > b.il:
            a, b = b, a
        n = N(a.il, b.ir, self.__func(a.val, b.val), a, b)
        return n

    def __func(self, a, b):
        return a + b

    def request(self, l, r):
        root = self.r
        answ = 0
        if l == r:
            while not (root.il == l and root.ir == r):
                if l >= root.l.il and r <= root.l.ir:
                    root = root.l
                else:
                    root = root.r
            answ = self.__func(answ, root.val)
            return answ

        if root.il == l and root.ir == r:
            return root.val
        f = True
        while f:
            if root.l.il <= l and root.l.ir >= r:
                root = root.l
            elif root.r.il <= l and root.r.ir >= r:
                root = root.r
            else:
                f = False
        left = root.l
        right = root.r
        while not left.il == l:
            if l < left.r.il:
                answ = self.__func(answ, left.r.val)
                left = left.l
            else:
                left = left.r
        answ = self.__func(answ, left.val)

        while not right.ir == r:
            if r > right.l.ir:
                answ = self.__func(answ, right.l.val)
                right = right.r
            else:
                right = right.l
        answ = self.__func(answ, right.val)
        return answ

    def req(self,l,r):
        return self.r.get_amount(l,r,self.__func)



'''
class ST:

    def __init__(self, arr, min_r):
        self.len = (math.ceil(math.log(len(arr), 2))) ** 2
        self.t = [0] * (4 * len(arr))
        for i in range(0, len(arr)):
            self.t[self.len + i] = int(arr[i] >= min_r)

        for i in range(self.len - 1, 0, -1):
            self.t[i] = self.__func(self.t[i * 2], self.t[i * 2 + 1])

    def __func(self, l, r):
        return l + r

    def request(self, left, right):
        l = self.len + left
        r = self.len + right
        ans = 0
        while l <= r:
            if l % 2 == 1:
                ans = self.__func(ans, self.t[l])
            if r % 2 == 0:
                ans = self.__func(ans, self.t[r])
            l = int((l + 1) / 2)
            r = int((r - 1) / 2)
        return ans'''

gradus = [0 for i in range(200002)]
recipes, min_r, questions = list(map(int, input().split()))
adds = []

for i in range(recipes):
    l, r = list(map(int, input().split()))
    if l == r:
        adds.append(l)
    else:
        gradus[l] -= 1
        gradus[r+1] += 1
counter = 0

for i in range(0, len(gradus)):
    if gradus[i] < 0:
        counter += abs(gradus[i])
    elif gradus[i] > 0:
        counter -= gradus[i]
    gradus[i] = counter
for i in adds:
    gradus[i] += 1

tree = ST(gradus, min_r)
res = []

for i in range(questions):
    l, r = list(map(int, input().split()))
    res.append(str(tree.request(l, r)))


print('\n'.join(res))

