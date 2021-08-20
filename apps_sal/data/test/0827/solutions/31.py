N = int(input())
T = input()
NUM = 10 ** 10
S = '110' * 2 * 10 ** 5
if '111' in T or '00' in T or '010' in T:
    print(0)
elif T == '1':
    print(NUM * 2)
elif T == '11':
    print(NUM)
else:
    zero_cnt = T.count('0')
    if T[-1] == '0':
        print(NUM - zero_cnt + 1)
    else:
        print(NUM - zero_cnt)
