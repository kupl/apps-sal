for __ in range(int(input())):
    ar = list(input())
    ans = []
    x = len(ar)
    for i in range(x - 4):
        if ar[i] + ar[i + 1] + ar[i + 2] + ar[i + 3] + ar[i + 4] == 'twone':
            ans.append(i + 3)
    for j in range(x - 4):
        if ar[j] + ar[j + 1] + ar[j + 2] == 'two' and ar[j + 3] + ar[j + 4] != 'ne':
            ans.append(j + 2)
        if ar[j + 2] + ar[j + 3] + ar[j + 4] == 'one' and ar[j] + ar[j + 1] != 'tw':
            ans.append(j + 4)
    if x > 2:
        if ar[x - 3] + ar[x - 2] + ar[x - 1] == 'two':
            ans.append(x - 1)
    if x > 3:
        if ar[x - 4] + ar[x - 3] + ar[x - 2] == 'two':
            ans.append(x - 2)
    if x > 2:
        if ar[0] + ar[1] + ar[2] == 'one':
            ans.append(2)
    if x > 3:
        if ar[1] + ar[2] + ar[3] == 'one':
            ans.append(3)
    print(len(ans))
    print(' '.join(map(str, ans)))
