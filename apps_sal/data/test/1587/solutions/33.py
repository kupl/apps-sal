N = int(input())
str = input()
r_sum = 0
for i in range(N):
    if str[i] == 'R':
        r_sum += 1
r_sum2 = 0
for i in range(r_sum):
    if str[i] == 'R':
        r_sum2 += 1
print(r_sum - r_sum2)
