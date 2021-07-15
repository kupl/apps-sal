A, B = map(int, input().split())

count = 0

for i in range(A, B+1):
    check = 0
    str_i = str(i)
    for j in range(0, (len(str_i)//2)+1):
        if int(str_i[j]) != int(str_i[-1-j]):
            check += 1
    if check == 0:
        count += 1

print("{}".format(count))
