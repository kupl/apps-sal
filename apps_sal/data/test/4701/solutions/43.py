n = int(input())
k = int(input())
a = 1
for i in range(n):
    if a<k:
        a = a*2
    else:
        a+=k
print(a)
