(A, B, C, D) = list(map(int, input().split()))
left_dish = A + B
right_dish = C + D
if left_dish > right_dish:
    print('Left')
elif left_dish < right_dish:
    print('Right')
elif left_dish == right_dish:
    print('Balanced')
