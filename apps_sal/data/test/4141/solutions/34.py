N = int(input())
my_list = list(input().split())
j = 0
for i in range(0, N):
    if int(my_list[i]) % 2 == 0:
        if int(my_list[i]) % 3 != 0 and int(my_list[i]) % 5 != 0:
            j += 1
if j != 0:
    print('DENIED')
else:
    print('APPROVED')
