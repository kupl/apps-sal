cat_num, unknown_animals, question_num_cat = map(int, input().split())

if cat_num <= question_num_cat <= cat_num + unknown_animals:
    print('YES')
else:
    print('NO')
