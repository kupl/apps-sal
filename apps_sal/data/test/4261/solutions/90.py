(a, b, c) = list(map(int, input().split()))
into_a = a - b
remain_c = c - into_a
if remain_c > 0:
    print(remain_c)
else:
    print(0)
