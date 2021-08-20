first = list(map(int, input().split()))
second = list(map(int, input().split()))
x_len = abs(first[0] - second[0])
y_len = abs(first[1] - second[1])
len_to_point = x_len + y_len
if len_to_point == 1:
    print(8)
elif x_len == 0 or y_len == 0:
    print((len_to_point - 1) * 2 + 8)
else:
    print((len_to_point - 2) * 2 + 8)
