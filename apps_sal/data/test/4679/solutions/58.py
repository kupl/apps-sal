from collections import deque
a=deque(input())
b=deque(input())
c=deque(input())

s={"a":a,"b":b,"c":c}
t="a"
while 1:
    if s[t]==deque():
        ans=t
        break
    t=s[t].popleft()
print(ans.upper())
