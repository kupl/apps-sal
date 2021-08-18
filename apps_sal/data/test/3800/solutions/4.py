from collections import Counter
a = int(input())
string = input()
arr = [0]
count1 = 0
count2 = 0
for i in range(len(string)):
    arr += [int(string[i])]
for i in range(1, len(arr)):
    arr[i] += arr[i - 1]
temparr = []
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        temparr += [(arr[j] - arr[i])]
sumset = Counter(temparr)
possums = 0
for i in (sumset):
    possums += sumset[i]
for i in (sumset):
    if i != 0 and a % i == 0 and i**2 != a:
        count1 += sumset[i] * sumset[a // i]
    elif i == 0 and a == 0:
        count1 += sumset[i] * possums
    elif i != 0 and a % i == 0 and i**2 == a:
        count2 += sumset[i] * sumset[a // i]

print(count1 + count2)
