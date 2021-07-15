def A():
    R,C = map(int, input().split())
    pasture = []
    for _ in range(R):
        line = input().replace('.','D')
        if 'WS' in line or 'SW' in line:
            return False
        pasture.append(line)

    #Check columns
    for i in range(C):
        column = ''.join([l[i] for l in pasture])
        if 'WS' in column or 'SW' in column:
            return False

    #Here it is ok
    return '\n'.join(pasture)

res = A()
if res:
    print('Yes')
    print(res)
else:
    print('No')
