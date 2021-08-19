n = int(input())
num = sorted(map(int, input().strip().split()))
powers_of_2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824]
num_dict = {}
for i in range(n):
    num_dict[num[i]] = num[i]
flag_two = False
flag_three = False
twos = []
threes = []
for i in range(n):
    curr = num[i]
    for power in powers_of_2:
        if num_dict.get(curr + power) is not None:
            flag_two = True
            twos = []
            twos.append(curr)
            twos.append(curr + power)
            if num_dict.get(curr + 2 * power) is not None:
                flag_three = True
                threes = []
                threes.append(curr)
                threes.append(curr + power)
                threes.append(curr + 2 * power)
                break
    if flag_three:
        break
if flag_three:
    print('3')
    print(' '.join(map(str, threes)))
elif flag_two:
    print('2')
    print(' '.join(map(str, twos)))
else:
    print('1')
    print(num[0])
