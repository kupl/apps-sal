n= int( str(input()) )
inp = input().strip().split()
inp = [int(i) for i in inp]
cur=0
for val in inp:
    cur = (cur + (val-1)%2 )%2
    if(cur == 1):
        print(1)
    else:
        print(2)


