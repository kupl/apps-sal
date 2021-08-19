ans1 = 'Heisei'
ans2 = 'TBD'
S = input().split('/')
if int(S[0]) > 2019 or (int(S[0]) == 2019 and int(S[1]) > 4):
    print(ans2)
else:
    print(ans1)
