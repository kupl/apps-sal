(sheep, wolves) = map(int, input().split())
if sheep > wolves:
    print('safe')
elif sheep <= wolves:
    print('unsafe')
