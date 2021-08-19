__author__ = 'Rakshak.R.Hegde'
'\nCreated on Dec 17 2014 PM 10:02\n\n@author: Rakshak.R.Hegde\n'
n = int(input())
a = list(map(int, input().split()))
minI = min(range(1, n - 1), key=lambda x: a[x + 1] - a[x - 1])
a.pop(minI)
maxI = max(range(1, n - 1), key=lambda x: a[x] - a[x - 1])
print(a[maxI] - a[maxI - 1])
