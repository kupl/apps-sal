__author__ = '1'


def minimize(m, s):
    if m == 1 and s == 0:
        return 0
    if s == 0:
        return -1
    array = [0 for i in range(m)]
    array[0] = 1

    currentFiller = m - 1
    val = s - 1
    for i in range(s - 1):
        if array[currentFiller] < 9:
            array[currentFiller] += 1
            val -= 1
        else:
            currentFiller -= 1
            if currentFiller >= 0:
                array[currentFiller] += 1
                val -= 1
            else:
                break
    if val == 0:
        s = ""
        for i in range(len(array)):
            s += str(array[i])
        return s
    else:
        return -1


def maximizeS(m, s):
    array = []
    for i in range(10**m):
        summ = 0
        st = str(i)
        for j in range(len(st)):
            summ += ord(str(st[j])[0]) - ord('0')
        if summ == s:
            array.append(i)
    array = sorted(array)
    if len(array) == 0:
        return -1
    else:
        return array[-1]


def minimizeS(m, s):
    array = []
    for i in range(10**m):
        if len(str(i)) == m:
            summ = 0
            st = str(i)
            for j in range(len(st)):
                summ += ord(str(st[j])[0]) - ord('0')
            if summ == s:
                array.append(i)
    array = sorted(array)
    if len(array) == 0:
        return -1
    else:
        return array[0]


def maximize(m, s):
    if m == 1 and s == 0:
        return 0
    if s == 0:
        return -1
    array = [0 for i in range(m)]
    array[0] = 1
    currentFiller = 0
    val = s - 1
    for i in range(s - 1):
        if array[currentFiller] < 9:
            array[currentFiller] += 1
            val -= 1
        else:
            currentFiller += 1
            if currentFiller < m:
                array[currentFiller] += 1
                val -= 1
            else:
                break
    if val == 0:
        s = ""
        for i in range(len(array)):
            s += str(array[i])
        return s
    else:
        return -1


for m in range(1, 6):
    for s in range(6):
        """
        if int(minimize(m, s)) != int(minimizeS(m, s)):
             print(m, s, minimize(m, s), minimizeS(m, s))
        if int(maximize(m, s)) != int(maximizeS(m, s)):
             print(m, s, maximize(m, s), maximizeS(m, s))
        """
        pass

m, s = list(map(int, input().split(' ')))
a = minimize(m, s)
b = maximize(m, s)
print(a, b)
