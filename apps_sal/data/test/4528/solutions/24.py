t = int(input())

for i in range(t):
    h , m = map(int , input().split())
    
    total = 24*60 - h*60 - m
    
    print(total)
