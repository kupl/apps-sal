a = [0, 0, 0]
a[0], a[1] = list(map(int, input().split()))
n = int(input()) - 1;
N = 1000000007
a[2] = a[1] - a[0];
if (n // 3) % 2: 
    print((-a[n % 3]) % N)
else:
    print(a[n % 3] % N)

