lun_array = [i for i in range(1, 10)]
k = int(input())
num_array = 9
seed_index = 0
while num_array < k:
    if lun_array[seed_index] % 10 != 0:
        lun_array.append(lun_array[seed_index] * 10 + lun_array[seed_index] % 10 - 1)
        num_array += 1
    lun_array.append(lun_array[seed_index] * 10 + lun_array[seed_index] % 10)
    num_array += 1
    if lun_array[seed_index] % 10 != 9:
        lun_array.append(lun_array[seed_index] * 10 + lun_array[seed_index] % 10 + 1)
        num_array += 1
    seed_index += 1
print(lun_array[k - 1])
