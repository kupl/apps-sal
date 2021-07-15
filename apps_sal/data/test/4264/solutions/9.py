N = int(input())

odd_num = 0
for i in range(1, N + 1):

    if len(str(i)) % 2 == 1:
        odd_num += 1

print(odd_num)
