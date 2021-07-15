__author__ = 'Esfandiar'
'''
import sys
input=sys.stdin.readline
n = int(input())
map(int,input().split())
list(map(int,input().split()))
'''
a=sorted(list(map(int,input().split())))
if a[0]+a[-1] == a[1]+a[-2] or a[0]+a[1]+a[2]==a[3]:
    print("YES")
else:
    print('NO')
