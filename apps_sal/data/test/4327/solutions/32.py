A, P = map(int,input().split())

P = P + A*3

apple_pie = 0

while  P>1:
    
    apple_pie = apple_pie + 1
    P = P - 2
    
print(apple_pie)
