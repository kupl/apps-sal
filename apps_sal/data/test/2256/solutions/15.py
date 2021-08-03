'''
Created on 2019. 9. 21.

@author: kkhh88
'''
#q = int(input())
#x, y = map(int,input().split(' '))
#print (' '.join(list(map(str, s))))

q = int(input())

for i in range(q):
    n = list(map(int, input().split(' ')))
    if n[2] > n[3]:
        ans = n[2] - n[3]
    else:
        ans = n[3] - n[2]

    ans = ans + n[1]

    if ans >= n[0]:
        ans = n[0] - 1

    print(ans)
