N, K = [int(i) for i in input().split()]
AS = [int(i) for i in input().split()]

visited = set([1])
cnt = 0
t = [1]
p = 1

while AS[p - 1] not in visited and cnt < K:
    a = AS[p - 1]
    visited.add(a)
    t.append(a)
    p = a
    cnt += 1

if cnt == K:
    print((t[-1]))
    import sys
    return

f_cnt = t.index(AS[p - 1])
loop_cnt = cnt + 1 - f_cnt
print((t[f_cnt + (K - f_cnt) % loop_cnt]))
