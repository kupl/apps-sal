import sys

def findMinSubSum(a, l):
    minim = sum(a[:l])

    current = minim
    for i in range(l, len(a)):
        current += a[i] - a[i - l]
        minim = min(current, minim)

    return minim

w, l = map(int, input().split())
a = list(map(int, input().split()))
print(findMinSubSum(a, l))
