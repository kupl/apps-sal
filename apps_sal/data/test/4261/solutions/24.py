S_list = list(map(int, input().split()))
a, b, c = S_list
if b + c - a > 0:
    print(b + c - a)
else:
    print(0)
