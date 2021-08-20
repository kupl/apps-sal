import collections
S = list(input())
deq = collections.deque(S)
Q = int(input())
mode = 1
for i in range(Q):
    f = input()
    f1 = f[0]
    if f1 == '1':
        mode = mode * -1
    else:
        (f1, F, C) = map(str, f.split())
        if F == '1' and mode == 1 or (F == '2' and mode == -1):
            deq.appendleft(C)
        if F == '2' and mode == 1 or (F == '1' and mode == -1):
            deq.append(C)
if mode == -1:
    deq.reverse()
ans = ''.join(deq)
print(ans)
