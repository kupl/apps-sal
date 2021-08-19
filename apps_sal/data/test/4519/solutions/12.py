t = int(input())
for _ in range(t):
    (n, k) = list(map(int, input().split()))
    s = input()
    ans = ''
    ones = 0
    zeros = 0
    flag = 0
    for i in range(n):
        if s[i] == '1':
            ones = ones + 1
        elif k >= ones:
            k = k - ones
            zeros = zeros + 1
        else:
            ans = '0' * zeros + '1' * (ones - k) + '0' + '1' * k + s[i + 1:]
            flag = 1
            break
    if flag == 0:
        ans = '0' * zeros + '1' * ones
    print(ans)
