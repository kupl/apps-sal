class Domino:
    def __init__(self, side1, side2, value, double, parts):
        self.side1 = side1
        self.side2 = side2
        self.value = value
        self.double = double
        self.parts = parts

    def __repr__(self):
        return str(self.side1) + '-' + str(self.side2) + '-' + str(self.double) + '-' + str(self.value) + '-' + '|'.join([str(i) for i in self.parts])

    def __add__(self, other):

        if self.side1 == other.side2:
            return Domino(self.side2, other.side1, self.value + other.value, self.side2 == other.side1, self.parts + other.parts)
        elif self.side1 == other.side1:
            return Domino(self.side2, other.side2, self.value + other.value, self.side2 == other.side2, self.parts + other.parts)
        elif self.side2 == other.side2:
            return Domino(self.side1, other.side1, self.value + other.value, self.side1 == other.side1, self.parts + other.parts)
        elif self.side2 == other.side1:
            return Domino(self.side1, other.side2, self.value + other.value, self.side1 == other.side2, self.parts + other.parts)
        else:
            return Domino(0, 0, 0, True, [-1])


def SortByValue(Domino):
    return Domino.value


def SortByDup(Domino):
    return Domino.double


def addbycolor(self, other, color):
    if self.side1 == color and other.side2 == color:
        return Domino(self.side2, other.side1, self.value + other.value, self.side2 == other.side1,
                      self.parts + other.parts)
    elif self.side1 == color and other.side1 == color:
        return Domino(self.side2, other.side2, self.value + other.value, self.side2 == other.side2,
                      self.parts + other.parts)
    elif self.side2 == color and other.side2 == color:
        return Domino(self.side1, other.side1, self.value + other.value, self.side1 == other.side1,
                      self.parts + other.parts)
    elif self.side2 == color and other.side1 == color:
        return Domino(self.side1, other.side2, self.value + other.value, self.side1 == other.side2,
                      self.parts + other.parts)
    else:
        raise Exception


def delcolor(l, num):

    p = 1
    while p == 1:
        p = 0
        for i in range(len(l) - 1):
            for j in range(i + 1, len(l)):

                if (l[i].side1 == num or l[i].side2 == num) and (l[j].side1 == num or l[j].side2 == num):
                    a = l.pop(i)
                    b = l.pop(j - 1)
                    ab = addbycolor(a, b, num)
                    l.append(ab)
                    p = 1
                    l.sort(key=SortByValue)
                    l.sort(key=SortByDup)
                    l.reverse()
                    break
            if p == 1:
                break

    l.sort(key=SortByValue)
    l.sort(key=SortByDup)
    l.reverse()
    return l


def getvalue(l):
    value = 0
    for i in l:
        value += i.value


n = int(input())
l = []
l_dup = []
for i in range(n):
    q, w, e = [int(el) for el in input().split()]
    if q == e + 100:
        l_dup.append(Domino(q, e, w, q == e, [i]))

    else:
        l.append(Domino(q, e, w, q == e, [i]))

l.sort(key=SortByValue)
l.sort(key=SortByDup)
l.reverse()

out = 0
s1 = [1, 2, 3, 4]
for i1 in s1:
    s2 = s1.copy()
    s2.remove(i1)
    for i2 in s2:
        s3 = s2.copy()
        s3.remove(i2)
        for i3 in s3:
            s4 = s3.copy()
            s4.remove(i3)
            for i4 in s4:
                l1 = l.copy()
                cc = len(l1)
                cont = 1
                while cont == 1:
                    cont = 0
                    l1 = delcolor(l1, i1)
                    l1 = delcolor(l1, i2)
                    l1 = delcolor(l1, i3)
                    l1 = delcolor(l1, i4)
                    if len(l1) < cc:
                        cc = len(l1)
                        cont = 1
                l1.sort(key=SortByValue)
                l1.reverse()
                out = max(out, l1[0].value)


print(out)
