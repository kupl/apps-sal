import sys

s = input()
t = input()

has = True

index_old = -1
for i in list(s):
    index = t.find(i, index_old+1)
    has = index > index_old 
    index_old = index
    if (not has):
        print(0)
        return

left = index_old + 1
index_old = len(t)
for i in s[::-1]:
    index = t.rfind(i,left,index_old)
    has = (index != -1 and index < index_old)
    index_old = index
    if (not has):
        print(0)
        return

print(index_old-left+1)

