(h, w) = map(int, input().split())
a_l = [list(input()) for _ in range(h)]
sub_array = []
for i in range(h):
    if '#' in a_l[i]:
        sub_array.append(a_l[i])
sub_array = [list(x) for x in zip(*sub_array)]
ans = []
for j in range(w):
    if '#' in sub_array[j]:
        ans.append(sub_array[j])
_ = [print(''.join(list(x))) for x in zip(*ans)]
