# In the name of Allah

from sys import stdin, stdout
input = stdin.readline

n = int(input())
m = int(input())

a = [int(input())for i in range(n)]

a.sort(reverse=True)

i = 0
cap = 0
while cap < m:
    cap += a[i]
    i += 1
stdout.write(str(i))
