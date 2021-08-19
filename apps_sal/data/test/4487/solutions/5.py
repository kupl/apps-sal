def f(x):
    f_list = []
    for i in x:
        f_list.append(i)
    return f_list


(a, b, c) = list(map(str, input().split(maxsplit=3)))
word_list_a = f(a)
word_list_b = f(b)
word_list_c = f(c)
if word_list_a.pop() == word_list_b[0] and word_list_b.pop() == word_list_c[0]:
    print('YES')
else:
    print('NO')
