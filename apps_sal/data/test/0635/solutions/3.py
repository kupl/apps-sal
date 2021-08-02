n, s = list(map(int, input().strip().split()))
ab = list(map(int, input().strip().split()))
bb = list(map(int, input().strip().split()))

s -= 1

if ab[0] == 0:
    print('NO')
else:
    if ab[s] == 1:
        print('YES')
    else:
        if bb[s] == 1:
            for i in range(s + 1, n):
                if ab[i] == 1 and bb[i] == 1:
                    print('YES')
                    break
            else:
                print('NO')
        else:
            print('NO')
