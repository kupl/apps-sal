n, m = list(map(int, input().split()))

flag = []


def letterwidth(i):
    res = flag[i][0]
    for item in flag[i]:
        if item != res:
            return None
    return res


def letterheight(i):
    res = flag[0][i]
    for j in range(n):
        if flag[j][i] != res:
            return None
    return res


for i in range(n):
    flag.append(input())

result = False

if(n % 3 == 0 and not result):
    w = n // 3
    letters = []
    for i in range(n):
        curres = letterwidth(i)
        letters.append(curres)
        if curres is None:
            break
    if(letters.count(None) == 0):
        answers = []
        counter = 0
        for i in range(3):
            res = letters[counter]
            answers.append(res)
            counter += 1
            for j in range(w - 1):
                if(letters[counter] != res):
                    letters.append(None)
                    break
                counter += 1
            if(letters.count(None) > 0):
                break
        if(letters.count(None) == 0):
            if(len(answers) == len(set(answers))):
                result = True
if(m % 3 == 0 and not result):
    w = m // 3
    letters = []
    for i in range(m):
        curres = letterheight(i)
        letters.append(curres)
        if curres is None:
            break
    if(letters.count(None) == 0):
        answers = []
        counter = 0
        for i in range(3):
            res = letters[counter]
            answers.append(res)
            counter += 1
            for j in range(w - 1):
                if(letters[counter] != res):
                    letters.append(None)
                    break
                counter += 1
            if(letters.count(None) > 0):
                break
        if(letters.count(None) == 0):
            if(len(answers) == len(set(answers))):
                result = True
if(result):
    print("YES")
else:
    print("NO")
