from math import sqrt
T = int(input())
for z in range(T):
    N = int(input())
    num = N
    i = 2
    nums = []
    found = 0
    s = int(sqrt(N))
    while i <= s:
        if num % i == 0:
            nums.append(i)
            num = num // i
            found += 1
            if found == 2:
                if num not in nums:
                    found = 3
                    nums.append(num)
                    break
        i += 1
    if found == 3:
        print('YES')
        print(*nums)
    else:
        print('NO')
