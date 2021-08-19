from sys import stdin, stdout
input = stdin.readline
for _ in range(int(input())):
    x = 10 ** 5
    (n, k) = list(map(int, input().split()))
    s = input()
    ans = 10 ** 9
    for i in range(n - k + 1):
        x = s[i:i + k]
        m = 0
        curr = ['R', 'G', 'B']
        for l in range(3):
            m = 0
            z = l
            for j in x:
                if j != curr[z]:
                    m += 1
                z += 1
                z %= 3
            ans = min(ans, m)
    print(ans)
