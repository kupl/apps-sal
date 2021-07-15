n = int(input())
f = [0] * 100002
t = list(map(int, input().split()))
for i in t : 
    f[i] += i
a = 0
b = 0
for i in f: 
    tmp = a
    a = max(a, b)
    b = tmp + i
print(a)
