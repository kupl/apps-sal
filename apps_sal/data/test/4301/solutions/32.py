(N, *D) = map(int, open(0).read().split())
S = sorted(D, reverse=True)
if S[1] == S[0]:
    [print(S[0]) for i in range(N)]
else:
    import numpy as np
    max_i = np.arange(N)[np.array(D) == S[0]]
    for i in range(N):
        if i == max_i:
            print(S[1])
        else:
            print(S[0])
