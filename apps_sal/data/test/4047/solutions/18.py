n = int(input())
a = list(map(int, input().split()))
ch = 0
nch = 0
for i in range(n):
    if a[i] % 2 == 0:
        ch += 1
    else:
        nch += 1
print(min(ch, nch))
