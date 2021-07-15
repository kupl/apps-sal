
"""
6 2
3 2 1 6 5 4
"""

n, k = map(int, input().split())
l = [int(x) for x in input().split()]
ans = []
minn = 123456567
key = 0
for i in range(k):
    j = i
    summ = 0
    while j < n:
        summ += l[j]
        j += k
    if(summ < minn):
        minn = summ
        key = i
print(key + 1)
