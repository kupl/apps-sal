n = int(input())
a = list(map(int, input().split(' ')))
a = sorted(a)
s = ''
for i in range(len(a)):
    s+=str(a[i])
    if i != len(a):
        s+=' '
print(s)
