input()
l = [ int(x) for x in input().split()]
l2 = [ int(x) for x in input().split()]

for ele in l:
    if ele in l2:
        print(ele,end=" ") 
