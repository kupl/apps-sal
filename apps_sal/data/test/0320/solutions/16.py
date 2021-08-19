"""
Created on Oct 10, 2013

@author: Anonymous
"""
n = int(input())
cnt = 0
suma = sumb = 0
for i in range(0, n):
    (a, b) = list(map(int, input().split()))
    if a % 2 != b % 2:
        cnt += 1
    (suma, sumb) = (suma + a, sumb + b)
if suma % 2 == 0 and sumb % 2 == 0:
    print(0)
elif suma % 2 != sumb % 2:
    print(-1)
elif cnt > 0:
    print(1)
else:
    print(-1)
