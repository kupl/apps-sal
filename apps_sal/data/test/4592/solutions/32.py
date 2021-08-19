n = int(input())
ji = {}
ans = 1
for i in range(n):
    tmp = i + 1
    j = 2
    while tmp != 1:
        if tmp % j == 0:
            if not j in ji:
                ji[j] = 0
            ji[j] += 1
            tmp /= j
        else:
            j += 1
for i in list(ji.values()):
    ans *= i + 1
print(ans % 1000000007)
