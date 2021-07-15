

MOD = 10**9 + 7
I = lambda:list(map(int,input().split()))

n, = I()
s = input()
res = ''
i = 0
j = 2
while i < n:
    print(s[i], end='')
    i += j
    j += 1
