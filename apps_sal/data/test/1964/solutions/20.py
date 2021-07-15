N = int(input())
kassa = list(map(int, input().split()))
i = 0
people = list([0] * N)
while i != N:
   people[i] = list(map(int, input().split()))
   i += 1
     
min_sec = 100000000000  
for human in people:
   sec = 0
   for tovar in human:
         sec += tovar * 5 + 15
   if min_sec > sec:
         min_sec = sec
           
print(min_sec)

