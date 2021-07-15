A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())

l=[A,B,C,D,E]
tot = 0
for i in l:
  tot+=-(-i//10)*10
  
a=max(map(lambda x: -(-x//10)*10-x, l))

print(tot-a)
