N, X, M = list(map(int, input().split()))
s = set()
l = list()
ans = 0

A = X
s.add(A)
l.append(A)
ans += A
index = 1
while True:
    Anext = (A * A) % M
    if Anext in s:
        break
    A = Anext
    s.add(A)
    l.append(A)
    ans += A
    index += 1
    if index == N:
        print(ans)
        return

Ai = Anext
index_Ai = l.index(Ai)
len_R = index - index_Ai
len_L = index - len_R
kurikaeshi = sum(l[len_L:])
ans += (N - index) // len_R * kurikaeshi
ans += sum(l[len_L:len_L + (N - index) % len_R])
print(ans)

