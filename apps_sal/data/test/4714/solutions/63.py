A, B = map(int, input().split())
ans_cou = 0
for i in range(A, B + 1):
    str_i = str(i)
    reverse_str_i = ''.join(list(reversed(str_i)))
    reverse_int_i = int(reverse_str_i)
    if i == reverse_int_i:
        ans_cou += 1
print(ans_cou)
