N, A, B, C = map(int, input().split())
ans = []
flag = True
cnt = 0
while True:
    cnt += 1
    if cnt > N:
        break
    s = input()
    if s == 'AB':
        if A == B == 0:
            flag = False
            break
        elif A == B == 1 and C == 0:
            if cnt == N:
                ans.append('A')
                break
            else:
                cnt += 1
                s = input()
                if s == 'AB':
                    ans.append('A')
                    ans.append('B')
                    continue
                elif s == 'AC':
                    ans.append('A')
                    ans.append('C')
                    B -= 1
                    C += 1
                    continue
                else:
                    ans.append('B')
                    ans.append('C')
                    A -= 1
                    C += 1
                    continue
        elif A >= B:
            A -= 1
            B += 1
            ans.append('B')
            continue
        else:
            B -= 1
            A += 1
            ans.append('A')
            continue
    elif s == 'BC':
        if B == C == 0:
            flag = False
            break
        elif B == C == 1 and A == 0:
            if cnt == N:
                ans.append('B')
                break
            else:
                cnt += 1
                s = input()
                if s == 'BC':
                    ans.append('B')
                    ans.append('C')
                    continue
                elif s == 'AB':
                    ans.append('B')
                    ans.append('A')
                    C -= 1
                    A += 1
                    continue
                else:
                    ans.append('C')
                    ans.append('A')
                    B -= 1
                    A += 1
                    continue
        elif B >= C:
            B -= 1
            C += 1
            ans.append('C')
            continue
        else:
            C -= 1
            B += 1
            ans.append('B')
            continue
    else:
        if C == A == 0:
            flag = False
            break
        elif C == A == 1 and B == 0:
            if cnt == N:
                ans.append('C')
                break
            else:
                cnt += 1
                s = input()
                if s == 'AC':
                    ans.append('C')
                    ans.append('A')
                    continue
                elif s == 'BC':
                    ans.append('C')
                    ans.append('B')
                    A -= 1
                    B += 1
                    continue
                else:
                    ans.append('A')
                    ans.append('B')
                    C -= 1
                    B += 1
                    continue
        elif A >= C:
            A -= 1
            C += 1
            ans.append('C')
            continue
        else:
            C -= 1
            A += 1
            ans.append('A')
            continue
if flag:
    print('Yes')
    for item in ans:
        print(item)
else:
    print('No')
