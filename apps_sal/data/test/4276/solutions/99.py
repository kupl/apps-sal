import operator
(N, T) = [int(i) for i in input().split()]
ct_list = [[int(i) for i in input().split()] for j in range(N)]
tmp = list([x for x in ct_list if operator.ge(T, x[1])])
ans = min(tmp, key=lambda x: x[0])[0] if len(tmp) != 0 else 'TLE'
print(ans)
