k = list(map(int, input().split()))

cnt1 = k.count(1)
cnt2 = k.count(2)
cnt3 = k.count(3)
cnt4 = k.count(4)

if cnt1 >= 1 or cnt2 >= 2 or cnt3 == 3 or (cnt4 == 2 and cnt2 == 1):
    print('YES')
else:
    print('NO')

