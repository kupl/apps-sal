def test(s):
    res = []
    for i in [[1, 12], [2, 6], [3, 4], [4, 3], [6, 2], [12, 1]]:
        a = [["O" for i in range(i[1])] for j in range(i[0])]
        for j in range(i[0]):
            for k in range(i[1]):
                a[j][k] = s[j * i[1] + k]
        if check(a):
            res.append(i)
    return res

def check(a):
    for i in range(len(a[0])):
        if not "O" in [a[j][i] for j in range(len(a))]:
            return True
    return False

t = int(input())
for i in range(t):
    s = input().strip()
    x = test(s)
    print(len(x), end=" ")
    for j in x:
        print(j[0], "x", j[1], sep="", end=" ")
    print()

