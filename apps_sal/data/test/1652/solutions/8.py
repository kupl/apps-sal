S = input()
i = 3
while i <= len(S):
    if i == 3:
        if S[-3:] == 'eam':
            i += 2
            if S[-i:-i + 2] == 'dr':
                i += 3
            else:
                print('NO')
                break
        elif S[-3:] == 'mer':
            i += 4
            if S[-i:-i + 4] == 'drea':
                i += 3
            else:
                print('NO')
                break
        elif S[-3:] == 'ase':
            i += 2
            if S[-i:-i + 2] == 'er':
                i += 3
            else:
                print('NO')
                break
        elif S[-3:] == 'ser':
            i += 3
            if S[-i:-i + 3] == 'era':
                i += 3
            else:
                print('NO')
                break
        else:
            print('NO')
            break
    elif S[-i:-i + 3] == 'eam':
        i += 2
        if S[-i:-i + 2] == 'dr':
            i += 3
        else:
            print('NO')
            break
    elif S[-i:-i + 3] == 'mer':
        i += 4
        if S[-i:-i + 4] == 'drea':
            i += 3
        else:
            print('NO')
            break
    elif S[-i:-i + 3] == 'ase':
        i += 2
        if S[-i:-i + 2] == 'er':
            i += 3
        else:
            print('NO')
            break
    elif S[-i:-i + 3] == 'ser':
        i += 3
        if S[-i:-i + 3] == 'era':
            i += 3
    else:
        print('NO')
        break
else:
    print('YES')
