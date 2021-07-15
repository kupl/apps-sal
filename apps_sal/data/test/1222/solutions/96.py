from collections import deque
K=int(input())
lunlundeque=deque()
for i in range(1,10):
    lunlundeque.append(i)
nowlunlun=0
index=0
while(index<K):
    index+=1
    nowlunlun=lunlundeque.popleft()
    if nowlunlun%10!=0:
        lunlundeque.append(nowlunlun*10+(nowlunlun%10)-1)
    lunlundeque.append(nowlunlun*10+nowlunlun%10)
    if nowlunlun%10!=9:
        lunlundeque.append(nowlunlun*10+(nowlunlun%10)+1)
print(nowlunlun)

