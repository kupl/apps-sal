pairs = []
for i in range(8):
    tmp = list(map(int, input().split()))
    pairs.append(tmp)
pairs.sort()


def judge():
    return (pairs[0][0] < pairs[3][0] < pairs[5][0] and
            pairs[0][1] < pairs[1][1] < pairs[2][1] and
            pairs[0][0] == pairs[1][0] == pairs[2][0] and
            pairs[3][0] == pairs[4][0] and
            pairs[5][0] == pairs[6][0] == pairs[7][0] and
            pairs[0][1] == pairs[5][1] and
            pairs[1][1] == pairs[6][1] and
            pairs[2][1] == pairs[7][1] and
            pairs[0][1] == pairs[3][1] and
            pairs[2][1] == pairs[4][1])


if judge():
    print('respectable')
else:
    print('ugly')
