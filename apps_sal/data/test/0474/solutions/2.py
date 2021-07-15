n = int(input())
a = list(map(int, input().split()))
q = max(a)
tmp = 0
num = 0
for i in range(n):
    if a[i] == q:
        tmp += 1
    else:
        num = max(num, tmp)
        tmp = 0
num = max(num, tmp)
print(num)

