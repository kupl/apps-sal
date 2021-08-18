A, B, C = map(int, input().split())

max_cnt = B // A
sat_cnt = C
if max_cnt < sat_cnt:
    print(max_cnt)
else:
    print(sat_cnt)
