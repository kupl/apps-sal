'''
Created on 30 dec. 2016

@author: Moldovan
'''

n = int(input())

for i in range(n):
    change, division = input().split()
    change = int(change)
    division = int(division)
    if i == 0:
        if division == 1:
            maxx = 10 ** 15
            minn = 1900
        else:
            maxx = 1899
            minn = -(10**10)
    if division == 1:
        if maxx < 1900:
            print("Impossible")
            return
        minn = max(minn, 1900)
        minn = minn + change
        maxx = maxx + change
    else:#div 2
        if minn >=1900:
            print("Impossible")
            return
        maxx = min(maxx, 1899)
        minn = minn + change
        maxx = maxx +change
if maxx > 10**10:
    print("Infinity")
else:
    print(maxx)
            

