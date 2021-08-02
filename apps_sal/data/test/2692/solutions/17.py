t = int(input())
for i in range(t):
    n, b = map(int, input().split())
    a = n - n // b
    if(n % b == 0):
        a = a + 1
    print(a)
