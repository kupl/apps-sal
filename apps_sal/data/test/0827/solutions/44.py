def solve():
    N = int(input())
    T = input()
    if N == 1:
        return 20000000000 if T == '1' else 10000000000
    T = T.replace('110', 'T')
    if T.startswith('10'):
        T = 'T' + T[2:]
    elif T.startswith('0'):
        T = 'T' + T[1:]
    if T.endswith('11'):
        T = T[:-2] + 'T'
    elif T.endswith('1'):
        T = T[:-1] + 'T'
    if all((t == 'T' for t in T)):
        return 10000000000 - (len(T) - 1)
    else:
        return 0


print(solve())
