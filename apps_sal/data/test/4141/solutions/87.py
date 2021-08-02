n = int(input())
num_list = list(map(int, input().split()))
bool = True
for i in range(n):
    x = num_list[i]
    if x % 2 == 0:
        bool = True
        if x % 3 != 0 and x % 5 != 0:
            bool = False
            break
if bool:
    print('APPROVED')
else:
    print('DENIED')
