

n = int(input())
s = input()
l = list(map(int, input().split()))
count = 0
mas = [False for i in range(n)]
pos = 0
ans = 'INFINITE'
for i in range(n):
    if mas[pos]:
        break
    else:
        mas[pos] = True
    if s[pos] == '<':
        if pos - l[pos] < 0:
            ans =  'FINITE'
        else:
            pos -= l[pos]
    else:
        if pos + l[pos] >= n:
            ans = 'FINITE'
        else:
            pos += l[pos]
print(ans)
