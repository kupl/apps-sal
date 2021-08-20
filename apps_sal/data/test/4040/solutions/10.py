line = input().split()
n = int(line[0])
m = int(line[1])
d = int(line[2])
line = input().split()
c = [int(x) for x in line]
if sum(c) + (len(c) + 1) * (d - 1) < n:
    print('NO')
else:
    cnt = n - sum(c)
    ans = []
    cnt2 = 0
    while cnt != 0:
        for i in range(d - 1):
            if cnt == 0:
                break
            ans.append(0)
            cnt -= 1
        if cnt2 >= len(c):
            break
        for i in range(c[cnt2]):
            ans.append(cnt2 + 1)
        cnt2 += 1
    while cnt2 != m:
        for i in range(c[cnt2]):
            ans.append(cnt2 + 1)
        cnt2 += 1
    print('YES')
    for ch in ans:
        print(str(ch), end=' ')
    print()
