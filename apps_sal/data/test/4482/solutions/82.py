n = int(input())
l = list(input().split())
sum = 0
min_sum = 10**10
num = 0
for i in range(-100, 101):
    for j in range(len(l)):
        sum += (int(l[j]) - i)**2
    if min_sum > sum:
        min_sum = sum
        num = i
    sum = 0

print(min_sum)
