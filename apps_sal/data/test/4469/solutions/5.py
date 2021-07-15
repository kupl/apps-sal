n = int(input())
shelf, L, R = {}, 0, 0
p, d = input().split()
shelf[d] = 0
for i in range(n-1):
    p, d = input().split()
    if p == 'L':
        shelf[d] = L - 1
        L -= 1 
    elif  p == 'R':
        shelf[d] = R + 1
        R += 1
    else:
        a = -(L - shelf[d])        
        b = R - shelf[d] 
        print(min(a, b))


