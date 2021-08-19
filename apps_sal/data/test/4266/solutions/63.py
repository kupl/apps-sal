(k, x) = map(int, input().split())
ans_list = [x]
original_x = x
for _ in range(k - 1):
    x = x - 1
    ans_list.append(x)
for _ in range(k - 1):
    if _ == 0:
        x = original_x
    x = x + 1
    ans_list.append(x)
ans_list.sort()
print(' '.join(map(str, ans_list)))
