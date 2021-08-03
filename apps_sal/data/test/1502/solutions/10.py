n = int(input())

arr = [15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7]

print(arr[n])
return
if n == 0:
    print(15)
    return

if n == 1:
    print(14)
    return

if n == 2:
    print(12)
    return

if n == 3:
    print(13)
    return

if n == 4:
    print(8)
    return

if n == 5:
    print(9)
    return

if n == 6:
    print(10)
    return

if n == 7:
    print(11)
    return

exit(228)
n = n ^ ((n & 1) << 1)

n = n ^ ((n & 1) << 1)
n = n ^ ((n & 2) << 1)

n = n ^ ((n & 1) << 1)
n = n ^ ((n & 2) << 1)
n = n ^ ((n & 4) << 1)

#n = n ^ ((n & 4) << 1) ^ ((n & 2) << 2) ^ ((n & 1) << 3)

print(n)


# 0011 -> 0001 -> 0101 -> 0101
