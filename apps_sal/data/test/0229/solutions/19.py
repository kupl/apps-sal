N = int(input())
A = set(list(map(int, input().split())))
if len(A) == 1:
    print('YES')
elif len(A) == 2:
    print('YES')
elif len(A) == 3:
    A = list(A)
    max_v = max(A)
    min_v = min(A)
    md_v = sum(A) - max_v - min_v
    if md_v * 2 == max_v + min_v:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
