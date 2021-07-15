s = input().split(' ')
n = int(s[0])
k = int(s[1])

if(k > n / 2):
    print(n * (n - 1) // 2)
else:
    print(2 * k * n - k * (2 * k + 1))
