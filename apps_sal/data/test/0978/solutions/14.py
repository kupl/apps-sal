__author__ = 'asmn'

k=int(input())
cnt=dict((i,0) for i in range(1,10))
for i in range(4):
    for j in input():
        if ord('1')<=ord(j)<=ord('9'):
            cnt[ord(j)-ord('0')]+=1
print('YES' if len(list([x for x in list(cnt.items()) if x[1]>2*k]))==0 else 'NO')

