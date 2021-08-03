s_position, a_store, b_store = list(map(int, input().split()))

dis_a_s = abs(a_store - s_position)
dis_b_s = abs(b_store - s_position)

if dis_b_s > dis_a_s:
    print('A')
elif dis_a_s > dis_b_s:
    print('B')
