import sys
from sys import stdin, stdout
n = int(stdin.readline())
coins = list(map(int, stdin.readline().split(' ')))
coins.sort()
x, f = list(map(int, stdin.readline().split(' ')))
flag1 = True
for i in range(len(coins)):
    if coins[i] > x:
        coins = coins[i:]; flag1 = False
        break

if flag1:
    coins = []
ctr = 0
'''
flag2=True
for i in range(len(coins)):
  if coins[i]>sc:
    coins=coins[i:]
    ctr+=(i+1)
    flag2=False
    break
if flag2:
  ctr=len(coins)
  coins=[]
'''
# print(coins)


def mainkaam(e):
    nonlocal x, f
    t1 = e // (x + f)
    t2 = e % (x + f)
    if t2 > x:
        return t1 + 1
    else:
        return t1


for i in coins:
    # print(mainkaam(i),i)
    ctr += (mainkaam(i))

print(ctr * f)
