day = 367
n = int(input())
male = [0] * day
female = [0] * day
for i in range(n):
    (sex, l, r) = input().split()
    if sex == 'M':
        for j in range(int(l), int(r) + 1):
            male[j] += 1
    else:
        for j in range(int(l), int(r) + 1):
            female[j] += 1
ans = 0
for i in range(1, day):
    ans = max(ans, min(male[i], female[i]))
print(ans * 2)
