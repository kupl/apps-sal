A, B = map(int, input().split())

if A % 3 == 0 or B % 3 == 0 or (A + B) % 3 == 0:  # 3で割って余りが出なければ、3匹平等に渡せる
    print('Possible')

else:
    print('Impossible')
