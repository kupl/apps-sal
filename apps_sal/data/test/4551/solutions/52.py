left_a, left_b, right_a, right_b = list(map(int, input().split()))

left_weight = left_a + left_b
right_weight = right_a + right_b

if left_weight == right_weight:
    print('Balanced')
elif left_weight > right_weight:
    print('Left')
elif right_weight > left_weight:
    print('Right')

