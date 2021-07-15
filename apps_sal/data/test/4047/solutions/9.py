def mi():
        return list(map(int, input().split()))
'''

'''
n = int(input())
a = list(mi())
for i in range(n):
    a[i] = a[i]%2
o = a.count(1)
z = n-o
print(min(o,z))

