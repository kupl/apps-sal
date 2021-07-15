n = int(input())
S = map(int,input().split())
Number = list(S)
count_number = 0

for i in range(n-2):
    if Number[0] > Number[1] > Number[2] or Number[2] > Number[1] > Number[0]:
        count_number += 1
    del Number[0]

print(count_number)
