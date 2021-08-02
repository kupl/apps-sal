import itertools

N = int(input())
S = [True if x == 'o' else False for x in input()]
S.append(S[0])
S.append(S[1])
lst = [None] * (N + 2)
for x0, x1 in itertools.product((True, False), repeat=2):
    lst[0], lst[1] = x0, x1
    for i in range(1, N + 1):
        lst[i + 1] = lst[i] ^ S[i] ^ lst[i - 1]
    if (lst[N], lst[N + 1]) == (lst[0], lst[1]):
        print((''.join(map(str, ('S' if x else 'W' for x in lst[:-2])))))
        break
else:
    print((-1))
