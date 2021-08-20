H = int(input())
count = 0
while H != 1:
    count += 1
    H = H >> 1
print(2 * 2 ** count - 1)
