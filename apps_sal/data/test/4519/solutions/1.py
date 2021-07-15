'''
https://codeforces.com/contest/1256/problem/D
'''


q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    s = list(input())
    l = 0
    for i in range(n):
        if k <= 0:
            break
        if s[i] == '0':
            if k >= i - l:
                s[i] = s[l]
                s[l] = '0'
                k -= i - l
                l += 1
            else:
                s[i] = s[i - k]
                s[i - k] = '0'
                break
    print(''.join(s))
