# coding: utf-8
# Your code here!

[s,t] = input().split()
[a,b] = list(map(int,input().split()))
u = input()

if s == u:
    a -= 1
elif t == u:
    b -= 1
    
print(a,b)
