import sys

n = int(input())
L = input().split()

zeros = 0
x = '1'

for num_str in L:
    z_count = num_str.count('0')
    if num_str.count('1') == 1 and z_count + 1 == len(num_str):
        zeros += len(num_str) - 1
    elif z_count == len(num_str):
        print(0)
        return
    else:
        x = num_str

print(x + '0' * zeros)

