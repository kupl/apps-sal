Q = int(input())
for q in range(Q):
    s = input()

    chet = []
    nechet = []
    for i in s:
        if int(i) % 2 == 0:
            chet.append(int(i))
        else:
            nechet.append(int(i))
    chet.append(10)
    nechet.append(10)

    i = 0
    j = 0
    ans = []
    while i < len(chet) and j < len(nechet):
        if i == len(chet) - 1 and j == len(nechet) - 1:
            break
        if chet[i] < nechet[j]:
            ans.append(chet[i])
            i += 1
        else:
            ans.append(nechet[j])
            j += 1

    print(*ans, sep='')
