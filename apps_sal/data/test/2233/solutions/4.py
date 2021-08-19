for i in ' ' * int(input()):
    n = int(input())
    s = input()
    t = input()
    counter = 0
    L = []
    for j in range(n):
        if s[j] != t[j]:
            counter += 1
            L.append(j)
    if counter != 0 and counter != 2:
        print('No')
        continue
    else:
        if counter == 0:
            print('Yes')
        else:
            (a, b) = L
            if s[a] == s[b] and t[a] == t[b]:
                print('Yes')
            else:
                print('No')
        continue
