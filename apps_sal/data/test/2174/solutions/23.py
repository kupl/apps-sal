n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
a.sort()
answ = 0
for i in range(n):
    answ += abs(a[i]-i-1)
print(answ)
