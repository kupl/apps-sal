import sys
input = sys.stdin.readline


def handle(type_, val_, u, g, S):
    if type_ == 'NOT':
        S.append(g[u][0])
    else:
        (v1, v2) = g[u]
        (val1, val2) = (Val[v1], Val[v2])
        if oper[type_](1 - val1, val2) != val_:
            S.append(v1)
        if oper[type_](val1, 1 - val2) != val_:
            S.append(v2)


def xor_(a, b):
    return a ^ b


def or_(a, b):
    return a | b


def not_(a):
    return 1 ^ a


def and_(a, b):
    return a & b


g = {}


def push(d, u, v):
    if u not in d:
        d[u] = []
    d[u].append(v)


n = int(input())
Val = [None] * n
Type = [''] * n
for i in range(n):
    arr = input().split()
    if len(arr) == 2:
        if arr[0] == 'IN':
            Type[i] = 'IN'
            Val[i] = int(arr[1])
        else:
            Type[i] = arr[0]
            push(g, i, int(arr[1]) - 1)
    else:
        (type_, v1, v2) = (arr[0], int(arr[1]), int(arr[2]))
        Type[i] = type_
        push(g, i, v1 - 1)
        push(g, i, v2 - 1)
oper = {}
oper['XOR'] = xor_
oper['OR'] = or_
oper['NOT'] = not_
oper['AND'] = and_
S = [0]
i = 0
while i < len(S):
    u = S[i]
    if u in g:
        for v in g[u]:
            S.append(v)
    i += 1
for u in S[::-1]:
    if u in g:
        type_ = Type[u]
        if len(g[u]) == 1:
            val_ = Val[g[u][0]]
            Val[u] = oper[type_](val_)
        else:
            (val_1, val_2) = (Val[g[u][0]], Val[g[u][1]])
            Val[u] = oper[type_](val_1, val_2)
ans = [0] * n
S = [0]
i = 0
while i < len(S):
    u = S[i]
    if u in g:
        (type_, val_) = (Type[u], Val[u])
        handle(type_, val_, u, g, S)
    i += 1
root_val = Val[0]
ans = [root_val] * n
for x in S:
    if Type[x] == 'IN':
        ans[x] = 1 - ans[x]
print(''.join([str(ans[x]) for x in range(n) if Type[x] == 'IN']))
