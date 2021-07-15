s = [i for i in input()]
n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
r = 0
j = 0
for i in range(len(s) // 2):
    while j < n and arr[j] <= i + 1:
        r += 1
        j += 1
    if r % 2 == 1:
        s[i], s[-i - 1] = s[-i - 1], s[i]
print(''.join(s))
