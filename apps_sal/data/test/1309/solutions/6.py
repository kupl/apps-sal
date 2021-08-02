n = int(input())
w = list(map(int, input().split()))
w.sort()
stab1 = 0
stab2 = 0
stab3 = 0
stabmin = 99999999999999999

for i in range(2 * n):
    for j in range(i + 1, 2 * n):
        temp = w.copy()
        del temp[i]
        del temp[j - 1]
        stab1 = 0

        for k in range(n - 1):
            stab1 += temp[2 * k + 1] - temp[2 * k]
        stabmin = min(stab1, stabmin)
print(stabmin)
