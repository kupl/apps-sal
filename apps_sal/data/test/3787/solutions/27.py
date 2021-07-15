N, A, B = list(map(int, input().split()))
if A*B < N or A+B-1 > N:
    print((-1))
else:
    array = [i for i in reversed(list(range(1, N+1)))]
    if A > 1:
        f = array[:B]
        r = array[B:]
        L = [f]
        span = len(r)//(A-1)
        rem = len(r)%(A-1)
        i = 0
        for _ in range(A-1):
            if rem > 0:
                L.append(r[i:i+span+1])
                rem -= 1
                i += span + 1
            else:
                L.append(r[i:i+span])
                i += span
        array = []
        for l in reversed(L):
            array += l
    print((' '.join([str(a) for a in array])))

