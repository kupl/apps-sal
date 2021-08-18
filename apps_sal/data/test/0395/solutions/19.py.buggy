powers = list(map(int, input().split()))
for first in range(len(powers)):
    for second in range(first + 1, len(powers)):
        for third in range(second + 1, len(powers)):
            sum1 = powers[first] + powers[second] + powers[third]
            used = set([first, second, third])
            sum2 = 0
            for i in range(len(powers)):
                if i not in used:
                    sum2 += powers[i]
            if sum1 == sum2:
                print("YES")
                return
print("NO")
