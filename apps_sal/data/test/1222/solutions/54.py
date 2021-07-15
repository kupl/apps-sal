import sys
input = sys.stdin.readline

#n = int(input())
#l = list(map(int, input().split()))

'''
a=[]
b=[]
for i in range():
    A, B = map(int, input().split())
    a.append(A)   
    b.append(B)'''

k=int(input())

from queue import Queue
que=Queue()
for i in range(1,10):
    que.put(str(i))
cnt=0
while True:
    a=que.get()
    cnt+=1
    #print(a)
    if cnt==k:
        print(a)
        return
    if a[-1]=="0":
        que.put(a+"0")
        que.put(a+"1")
    elif a[-1]=="9":
        que.put(a+"8")
        que.put(a+"9")
    else:
        #ac=int(a[-1])
        que.put(a+chr(ord(a[-1])-1))
        que.put(a+a[-1])
        que.put(a+chr(ord(a[-1])+1))

