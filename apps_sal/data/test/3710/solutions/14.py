import math
def gcd(a, b):
    if b == 0:
        return a;
    else:
        return gcd(b, a % b);

def lcm(a, b):
    return a * b // math.gcd(a, b);

def solve(n, k):
    ans = 1;
    a = list(map(int, input().split()));
    #print(a);
    for i in range(n):
        ans = math.gcd(k, lcm(ans, a[i]));
    return ans == k;

while True:
    try:
        n, k = list(map(int, input().split()));
        p = solve(n, k);
        if p:
            print("Yes");
        else:
            print("No");
    except EOFError:
        break

