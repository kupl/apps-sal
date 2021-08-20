details = input().split()
N = int(details[0])
L = int(details[1])
counter = 0
new_list = []
number = 0
checker = True
for i in range(N):
    counter += L
    new_list.append(L + i)
    if number == 0 and L + i >= 0 and (checker == True):
        number += L + i
        checker = False
    elif number == 0 and i == N - 1 and (checker == True):
        number += L + i
        checker = False
print(sum(new_list) - number)
