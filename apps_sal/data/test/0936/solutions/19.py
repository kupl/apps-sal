n = int(input())
likes_str = input()
likes = likes_str.split()
photo = {}
max_val = 0
max_num = 0
for i in range(0, n):
    photo_num = int(likes[i])
    if photo_num in photo:
        photo[photo_num] += 1
    else:
        photo[photo_num] = 1
    if photo[photo_num] > max_val:
        max_val = photo[photo_num]
        max_num = photo_num
print(max_num)
