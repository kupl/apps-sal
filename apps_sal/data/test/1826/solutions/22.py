n = int(input())
turns = input().strip()
c = 1
res = len(turns)
while c < (len(turns)):
    if turns[c]!= turns[c-1]:
        res -=1
        c+=1
    c+=1

print(res)




