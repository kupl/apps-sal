# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# import math
# from itertools import *
# import random
# import calendar
import datetime
# import webbrowser

# f = open("input.txt", 'r')
# g = open("output.txt", 'w')
# n, m = map(int, f.readline().split())

n, k = list(map(int, input().split()))
dislike = list(map(int, input().split()))
while True:
    for i in str(n):
        if int(i) not in dislike:
            continue
        else:
            break
    else:
        break
    n += 1
print(n)
