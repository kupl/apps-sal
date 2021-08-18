from copy import deepcopy
iarr = list(map(int, input().split()))
n = iarr[0]
m = iarr[1]
tar = list(map(int, input().split()))
freq = [0 for i in range(101)]
for i in range(n):
    rem = m - tar[i]
    count = 0
    counthr = 0
    for j in range(1, 101):
        afteradd = counthr + freq[j] * j
        if afteradd > rem:
            count += (rem - counthr) // j
            counthr += count * j
            break
        elif afteradd == rem:
            counthr = afteradd
            count += freq[j]
            break
        else:
            counthr = afteradd
            count += freq[j]

    freq[tar[i]] += 1
    print(i - count, end=" ")
print()
