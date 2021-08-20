n = int(input())
st = input()
if n % 4 != 0:
    print('===')
else:
    (ca, cb, cc, cd) = (0, 0, 0, 0)
    av = n // 4
    for i in range(len(st)):
        if st[i] == 'A':
            ca += 1
        elif st[i] == 'C':
            cb += 1
        elif st[i] == 'G':
            cc += 1
        elif st[i] == 'T':
            cd += 1
    if ca > av or cb > av or cc > av or (cd > av):
        print('===')
    else:
        (aa, ab, ac, ad) = (av - ca, av - cb, av - cc, av - cd)
        ss = aa * 'A' + ab * 'C' + ac * 'G' + ad * 'T'
        cnt = 0
        for i in range(len(st)):
            if st[i] == '?':
                print(ss[cnt], end='')
                cnt += 1
            else:
                print(st[i], end='')
