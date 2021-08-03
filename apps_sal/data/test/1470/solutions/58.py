x = int(input())

rt = (x // 11) * 2
tmp = x % 11
if tmp > 6:
    rt += 1
    tmp -= 6

print(rt + 1 if tmp > 0 else rt)
