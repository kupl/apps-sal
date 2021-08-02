def gcd(a, b):
    if(a == 0 or b == 0): return a + b
    else: return gcd(b, a % b);


l, r = list(map(int, input().split()))

r = r + 1
for a in range(l, r):
    for b in range(a + 1, r):
        for c in range(b + 1, r):
            if(gcd(a, b) == 1 and gcd(b, c) == 1 and gcd(a, c) != 1):
                print(str(a) + " " + str(b) + " " + str(c))
                return

print(-1)
