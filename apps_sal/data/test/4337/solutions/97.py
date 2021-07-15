N=int(input())
S=list(input().split())
for c in S:
    if c=='Y':
        print("Four")
        break
else:
    print("Three")

