N = int(input())
A = list(map(int, input().split()))
ans_list = []

for n in A:
    temp = n
    count = 0
    while temp % 2 == 0:
        temp /= 2
        count = count + 1
    ans_list.append(count)

print(min(ans_list))
