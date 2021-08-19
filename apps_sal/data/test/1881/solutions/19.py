(n, k) = [int(x) for x in input().split()]
ns = [int(x) for x in input().split()]
done = [None] * 256
ans = [None] * n
for i in range(n):
    c = ns[i]
    if done[c] == None:
        j = c
        while True:
            if j < 0 or c - j >= k or (done[j] != None and done[j] != -1):
                break
            j -= 1
        j += 1
        for kk in range(k):
            if kk + j >= 256 or (done[kk + j] != None and done[kk + j] != -1):
                break
            if kk + j <= c:
                done[kk + j] = j
            else:
                done[kk + j] = -1
    elif done[c] == -1:
        j = c
        while True:
            if done[j] != None and done[j] != -1:
                break
            j -= 1
        a = done[j]
        for kk in range(j, c + 1):
            done[kk] = a
    else:
        pass
    ans[i] = done[c]
ans = [str(x) for x in ans]
print(' '.join(ans))
