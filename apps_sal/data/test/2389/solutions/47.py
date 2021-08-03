def main():
    N, A, B, C = list(map(int, input().split(' ')))
    S = [input() for _ in range(N)]
    D = {
        'AB': A + B,
        'BC': B + C,
        'AC': A + C
    }
    ans = list()
    for i, s in enumerate(S):
        if D[s] == 0:
            print('No')
            return
        if s == 'AB':
            if (D['BC'] < D['AC']) or \
                    (i < N - 1 and S[i + 1] == 'BC' and D['BC'] == D['AC'] == 1):
                ans.append('B')
                D['BC'] += 1
                D['AC'] -= 1
            else:
                ans.append('A')
                D['BC'] -= 1
                D['AC'] += 1
        elif s == 'BC':
            if (D['AB'] < D['AC']) or \
                    (i < N - 1 and S[i + 1] == 'AB' and D['AB'] == D['AC'] == 1):
                ans.append('B')
                D['AB'] += 1
                D['AC'] -= 1
            else:
                ans.append('C')
                D['AB'] -= 1
                D['AC'] += 1
        else:  # s == 'AC'
            if (D['AB'] < D['BC']) or \
                    (i < N - 1 and S[i + 1] == 'AB' and D['AB'] == D['BC'] == 1):
                ans.append('A')
                D['AB'] += 1
                D['BC'] -= 1
            else:
                ans.append('C')
                D['AB'] -= 1
                D['BC'] += 1
    print('Yes')
    for a in ans:
        print(a)


def __starting_point():
    main()


__starting_point()
