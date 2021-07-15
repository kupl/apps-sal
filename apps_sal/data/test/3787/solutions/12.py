def distribute(n, person, min, max, mode="even"):
    # n 個を person 人に分配する
    # 返り値は [[a (個), a 個もらう人数], ...]
    # 分配できないときは None を返す
    if person==0 and n==0:
        return []
    elif not min*person <= n <= max*person:
        return None
    elif mode=="even":
        q, m = divmod(n, person)
        if m==0:
            return [[q, person]]
        else:
            return [[q, person-m], [q+1, m]]
    elif mode=="greedy":
        if max==min:
            return [[max, person]]
        n -= min * person
        q, m = divmod(n, max-min)
        if m==0:
            return [[min, person-q], [max, q]]
        else:
            return [[min, person-1-q], [min+m, 1], [max, q]]
    else:
        raise ValueError("'mode' must be 'even' or 'greedy'.")

import numpy as np
N, A, B = list(map(int, input().split()))
Ans = np.arange(N, 0, -1, dtype=np.int64)
Ans[:A] = np.flipud(Ans[:A])
c = N-A
D = distribute(c, B-1, min=1, max=A, mode="greedy")
if D is None:
    print((-1))
    return
idx = A
for p, n in D:
    for n_ in range(n):
        Ans[idx:idx+p] = np.flipud(Ans[idx:idx+p])
        idx += p
print((" ".join(str(int(a)) for a in Ans)))

