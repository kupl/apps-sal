n, k = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
res = 0
for i in a:
    res += (i+k-1) // k

print((res+1)//2)
