(rectangle1_scale1, rectangle1_scale2, rectangle2_scale1, rectangle2_scale2) = list(map(int, input().split()))
big_rectangle_area = max(rectangle1_scale1 * rectangle1_scale2, rectangle2_scale1 * rectangle2_scale2)
print(big_rectangle_area)
