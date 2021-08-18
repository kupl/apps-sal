N = int(input())
T = input()

l = 10**10

bad_cases = ['00', '010', '111']

for i in bad_cases:
    if i in T:
        print(0)
        return

if '0' in T:
    zero_cnt = T.count('0')
    if T[N - 1] == '0':
        print(l - zero_cnt + 1)
    else:
        print(l - zero_cnt)
elif T == '1':
    print(l * 2)
else:
    print(l)
