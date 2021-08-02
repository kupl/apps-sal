def main(r, c, seq):
    answer = 0
    for i in range(r):
        k = seq[i].count(1)
        if k == 0:
            for j in range(c):
                item = seq[i][j]
                if item == 0:
                    seq[i][j] = 2
                    answer += 1
    for i in range(c):
        temp = 0
        for j in range(r):
            item = seq[j][i]
            if item == 0:
                temp += 1
            elif item == 1:
                temp = 0
                break

        answer += temp

    return answer


def init():
    r, c = list(map(int, input().split()))
    seq = []
    for i in range(r):
        temp = []
        for item in input():
            if item == 'S':
                temp += [1]
            else:
                temp += [0]
        seq.append(temp)

    print(main(r, c, seq))


init()
