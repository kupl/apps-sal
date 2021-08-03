from collections import Counter

N = int(input())
A = Counter(list(map(int, input().split())))

res = 0
for values, counts in list(A.items()):
    if(values > counts):
        res += counts
    elif(values < counts):
        res += counts - values
print(res)
