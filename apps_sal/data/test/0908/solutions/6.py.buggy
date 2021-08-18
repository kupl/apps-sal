n = int(input())
c = [int(x) for x in input().split()]
sumc = [0, 0]
lastWord = ['', '']
t = [True, True]
newT = [True, True]
newSumc = [0, 0]
for i in range(n):
    s1 = input()
    s = s1
    if (t[0] and (s >= lastWord[0])) and (t[1] and (s >= lastWord[1])):
        newSumc[0] = min(sumc[1], sumc[0])
        newT[0] = True
    elif ((t[0] and (s >= lastWord[0]))):
        newSumc[0] = sumc[0]
        newT[0] = True
    elif t[1] and (s >= lastWord[1]):
        newSumc[0] = sumc[1]
        newT[0] = True
    else:
        newT[0] = False
    s2 = s1[::-1]
    s = s2
    if t[0] and (s >= lastWord[0]):
        if t[1] and (s >= lastWord[1]):
            newSumc[1] = min(sumc[0], sumc[1]) + c[i]
        else:
            newSumc[1] = sumc[0] + c[i]
        newT[1] = True
    elif t[1] and (s >= lastWord[1]):
        newSumc[1] = sumc[1] + c[i]
        newT[1] = True
    else:
        newT[1] = False
    lastWord = [s1, s2]
    t[0] = newT[0]
    t[1] = newT[1]
    sumc[0] = newSumc[0]
    sumc[1] = newSumc[1]
    if not(t[0] or t[1]):
        print(-1)
        return
if (t[0] and t[1]):
    print(min(sumc[0], sumc[1]))
elif (t[0]):
    print(sumc[0])
elif (t[1]):
    print(sumc[1])
