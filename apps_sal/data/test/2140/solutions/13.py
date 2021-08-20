st = str(input())
s = []
s = list(st)
n = int(input())
b = []
b = list(map(int, input().split()))
b.sort()
l = len(b)
k = len(s) - 1
m = int((k + 2) / 2)
b.append(m + 1)
while l:
    if l <= 0:
        break
    if l & 1 == 1:
        for i in range(b[l - 1] - 1, b[l] - 1):
            tem = s[i]
            s[i] = s[k - i]
            s[k - i] = tem
    l -= 1
for i in range(0, k + 1):
    print(s[i], end='')
