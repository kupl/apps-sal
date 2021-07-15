t = int(input())

for _ in range(t):
    s1 = input()[::-1]
    s2 = input()[::-1]

    pos2 = -1
    for i, c in enumerate(s2):
        if c == '1':
            pos2 = i
            break

    if pos2 == -1:
        print(0)
        continue
    
    ok = False
    for j in range(pos2, len(s1)):
        if s1[j] == '1':
            print(j - pos2)
            ok = True
            break

    if not ok:
        print(0)
