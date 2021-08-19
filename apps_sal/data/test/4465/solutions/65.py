(len_a, len_b) = list(map(int, input().split()))
total_area = len_a * len_b
road = len_a + len_b - 1
print(total_area - road)
