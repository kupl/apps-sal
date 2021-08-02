N = int(input())

cnt = 0

while 2 ** cnt <= N:
    cnt += 1

cnt -= 1

print(2**cnt)
