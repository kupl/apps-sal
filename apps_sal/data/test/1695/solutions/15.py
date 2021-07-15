n, m = list(map(int,input().split()))

a = [[0 for j in range(5)] for i in range(m)]

for i in range(n):
    s = input()
    for j in range(m):
        a[j][ord(s[j]) - ord('A')] += 1
sum1  = 0
b=  list(map(int,input().split()))
for i in range(m):
    sum1 += b[i] * max(a[i])
print(sum1)

