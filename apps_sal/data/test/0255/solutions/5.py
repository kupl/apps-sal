n = int(input())
ad = list(sorted(list(map(int, input().split()))))
m = int(input())
am = list(sorted(list(map(int, input().split()))))
i = 0
j = 0
sum1 = 0
while i < n and j < m:
    if abs(ad[i] - am[j]) < 2:
        sum1 += 1
        i += 1
        j += 1
    elif ad[i] < am[j]:
        i += 1
    else:
        j += 1
print(sum1)

