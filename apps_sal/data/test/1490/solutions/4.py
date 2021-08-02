n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A.append(10**9 + 1)
B = []
answer = 0
cou = 0
per = 1
per2 = True
for i in range(n + 1):
    if per2 == False:
        break
    while per != A[i]:

        answer += per
        if answer <= m:
            cou += 1
            B.append(per)
        else:
            print(cou)
            print(' '.join(map(str, B)))
            per2 = False
            break
        per += 1

    per += 1
