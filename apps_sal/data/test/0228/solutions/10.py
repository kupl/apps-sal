n=int(input())
piles = list(map(int,input().split()))
if(piles.count(min(piles))>n/2):
    print("Bob")
else:
    print("Alice")

