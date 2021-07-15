h, w = map(int, input().split())
c = [list(input()) for i in range(h)]
for i in c:
    for j in i:
        print(j, end ='')
    print('')
    for j in i:
        print(j, end ='')
    print('')
