n = int(input())
lst_a = [int(i) for i in input().split()]
lst_b = [int(i) for i in input().split()]
j = 0
flag = True
for i in range(n):
    if i > 0:
        if lst_a[i] != lst_a[i - 1]:
            j = 0
    if lst_a[i] != lst_b[i]:
        continue
    else:
        flag = False
        while j != n:
            if lst_a[i] != lst_b[j] and lst_a[j] != lst_b[i]:
                lst_b[i], lst_b[j] = lst_b[j], lst_b[i]
                flag = True
                break
            j += 1
        if not flag:
            break
if not flag:
    print('No')
else:
    print('Yes')
    lst_b = [str(i) for i in lst_b]
    print(' '.join(lst_b))
