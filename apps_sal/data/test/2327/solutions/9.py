'''
5
5
7
11
1
2000000000000
'''

for _ in range(int(input())):
    n = int(input())
    ind = 0
    ans=0
    while n//(2**ind):
        ans+= n//(2**ind)
        ind+=1
    print(ans)


