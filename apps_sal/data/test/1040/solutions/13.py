from collections import deque

n = int(input())
S = input()

index = 0
cnt = 0

q = deque()
q.append(index)

for s in S:
        
    if(s == "f"):
        index = 1
        q.append(index)
    elif(s == "o"):
        index = q.pop()
        if(index == 1):
            index = 2
        else:
            index = 0
        q.append(index)
    elif(s == "x"):
        index = q.pop()
        if(index == 2):
            cnt += 1
        else:
            index = 0
            q.append(index)
    else:
        index = q.pop()
        index = 0
        q.append(index)
ans = n - 3 * cnt
print(ans)
