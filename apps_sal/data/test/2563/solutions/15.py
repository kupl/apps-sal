t = int(input())
for j in range(t):
    s = input()
    first = []
    second = []
    for i in range(len(s)):
        if int(s[i]) % 2:
            first.append(int(s[i]))
        else:
            second.append(int(s[i]))
    i_f = 0
    i_s = 0
    while i_f < len(first) and i_s < len(second):
        if first[i_f] < second[i_s]:
            print(first[i_f], end = '')
            i_f += 1
        else:
            print(second[i_s], end = '')
            i_s += 1
    while i_f < len(first):
        print(first[i_f], end = '')
        i_f += 1
    while i_s < len(second):
        print(second[i_s], end = '')
        i_s += 1
    print()

