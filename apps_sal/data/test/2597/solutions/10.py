'''
Created on 2019. 9. 21.

@author: kkhh88
'''
#q = int(input())
#x, y = map(int,input().split(' '))
#print (' '.join(list(map(str, s))))

q = int(input())
for _ in range(q):
    n = int(input())
    s = list(map(int, input().split(' ')))
    s.sort(reverse=True)
    cnt = 0
    for d in s:
        if d >= cnt + 1:
            cnt = cnt + 1
        else:
            break

    print(cnt)
