(H, W) = input().split()
dummy_list = ['.'] * (int(W) + 2)
square_list = []
square_list.append(dummy_list)
for i in range(int(H)):
    wide_list = ['.']
    wide_list = wide_list + list(input())
    wide_list.append('.')
    square_list.append(wide_list)
square_list.append(dummy_list)
ans = 'Yes'
for i in range(1, int(H) + 1):
    for j in range(1, int(W) + 1):
        before_list = square_list[i - 1]
        center_list = square_list[i]
        after_list = square_list[i + 1]
        if center_list[j] == '.':
            continue
        if before_list[j] == '.' and center_list[j - 1] == '.' and (center_list[j + 1] == '.') and (after_list[j] == '.'):
            ans = 'No'
print(ans)
