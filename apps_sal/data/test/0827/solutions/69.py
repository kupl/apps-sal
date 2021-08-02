N = int(input())
T = input()

l = len(T)

if l == 1:
    if T == "1":
        print(2 * 10**10)
    elif T == '0':
        print(10**10)
elif l == 2:
    if T == '11':
        print(10**10)
    elif T == '10':
        print(10**10)
    elif T == '01':
        print(10**10 - 1)
    elif T == '00':
        print(0)
elif l >= 3:
    s = '110'
    flag = False
    flag110 = False
    index = 0
    for j in range(3):
        index = j
        f = True
        for i in range(l):
            if s[index] != T[i]: f = False
            index = (index + 1) % 3

        if f: flag = True
        if j == 0 and f and l % 3 == 0: flag110 = True
    if flag110:
        print(10**10 - l // 3 + 1)
    elif flag and T[0] == '0':
        print(10**10 - (l + 1) // 3)
    elif flag:
        print(10**10 - l // 3)
    else: print(0)
