def read_ints():
    return list(map(int, input().strip().split()))


(k, a, b, v) = read_ints()
z = (a + v - 1) // v
used_boxes = 0
free_div = b
last_box_sec = float('inf')
while z:
    if last_box_sec < k and free_div > 0:
        last_box_sec += 1
        free_div -= 1
    else:
        used_boxes += 1
        last_box_sec = 1
    z -= 1
print(used_boxes)
