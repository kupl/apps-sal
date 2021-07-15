import sys
b = int(input())
num = 100
year =0
for i in range(10**18):
    num += num//100
    year +=1
    if int(num) >=b:
        print(year)
        return

