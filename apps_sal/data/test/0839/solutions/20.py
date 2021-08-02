__author__ = 'Lipen'


def main():
    g = []
    for i in range(5):
        g.append(list(map(int, input().split())))

    already = []
    smax = 0
    for q1 in range(5):
        for q2 in range(5):
            if q2 not in [q1]:
                for q3 in range(5):
                    if q3 not in [q1, q2]:
                        for q4 in range(5):
                            if q4 not in [q1, q2, q3]:
                                for q5 in range(5):
                                    if q5 not in [q1, q2, q3, q4]:
                                        s = g[q1][q2] + g[q2][q1] + 2 * g[q3][q4] + 2 * g[q4][q3] + g[q2][q3] + g[q3][q2] + 2 * g[q4][q5] + 2 * g[q5][q4]
                                        if s > smax:
                                            smax = s
    print(smax)


main()
