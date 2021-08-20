(h, w) = map(int, input().split())
flag = False
ans = []
for i in range(h):
    A = list(map(int, input().split()))
    if i % 2 == 0:
        r = range(w)
    else:
        r = range(w - 1, -1, -1)
    for j in r:
        a = A[j]
        if (i > 0 or j > 0) and flag:
            ans.append(f'{prev_i + 1} {prev_j + 1} {i + 1} {j + 1}')
        if flag:
            if a % 2 == 0:
                flag = True
            else:
                flag = False
        elif a % 2 == 0:
            flag = False
        else:
            flag = True
        prev_i = i
        prev_j = j
print(len(ans))
print('\n'.join(ans))
