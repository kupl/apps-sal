t = int(input())
el = [[1,2,3,4,1,2,3,4],[5,6,7,8,5,6,7,8],[9,10,11,12,9,10,11,12],[13,14,15,16,13,14,15,16],[1,2,3,4,1,2,3,4],[5,6,7,8,5,6,7,8],[9,10,11,12,9,10,11,12],[13,14,15,16,13,14,15,16]]
for x in range(t):
    arr = [[]for i in range(8)]
    for i in range(8):
        s = input()
        for j in range(len(s)):
            arr[i].append(s[j])
    l = 0
    for i in range(8):
        for j in range(8):
            if l == 0:
                if arr[i][j] == 'K':
                    k1 = el[i][j]
                    l = 1
            else:
                if arr[i][j] == 'K':
                    k2 = el[i][j]
                    break
    if k1 == k2:
        print('YES')
    else:
        print('NO')
    if x != t-1:
        y = list(map(int, input().split()))
