'''
Name : Jaymeet Mehta
codeforces id :mj_13
Problem : 
'''
from sys import stdin, stdout
test = int(stdin.readline())
for _ in range(test):
    n, x = map(int, stdin.readline().split())
    n -= 2
    ans = 1
    while(n > 0):
        n -= x
        ans += 1
    print(ans)
