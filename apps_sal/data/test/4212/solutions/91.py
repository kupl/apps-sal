from sys import stdin
import itertools

N, M, Q = [int(x) for x in stdin.readline().rstrip().split()]
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q

for i in range(Q):
    a[i], b[i], c[i], d[i] = [int(x) for x in stdin.readline().rstrip().split()]
    a[i] -= 1
    b[i] -= 1

ans = 0

#print(list(itertools.combinations( list(range(1, M+1)), N)))
for A in itertools.combinations_with_replacement(list(range(1, M + 1)), N):
    # print("A:" + str(A))  # (1, 2, 3), (1, 2, 4) ...

    cur = 0

    for i in range(Q):
        if (A[b[i]] - A[a[i]] == c[i]):
            #print("a:" + str(a[i]) + " / b:" + str(b[i]) + " / A[b[i]]:" + str(A[b[i]]) + " / A[a[i]]:" + str(A[a[i]]) + " / c[i]:" + str(c[i]) + " / d[i]:" + str(d[i]) + " -> Matched" )
            cur += d[i]

    #print("tmp ans for A:" + str(cur))

    if (ans < cur):
        #print("Overwrite ans")
        ans = cur

print(ans)
