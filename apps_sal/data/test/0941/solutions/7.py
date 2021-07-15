b, k = list(map(int, input().split()))
X = [int(a) for a in input().split()]

if b % 2 == 1:
    r = sum(X) % 2
else:
    r = X[-1] % 2
    
if r == 0:
    print("even")
else:
    print("odd")


