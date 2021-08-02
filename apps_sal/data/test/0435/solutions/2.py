__author__ = 'Utena'
n, k = map(int, input().split())
s = ['0'] + list(input())
beauty = 0
i = 0
j = 0
a = 0
b = 0
while i < n:
    i += 1
    if s[i] == 'a':
        a += 1
    if s[i] == 'b':
        b += 1
    while min(a, b) > k:
        j += 1
        if s[j] == 'a':
            a -= 1
        if s[j] == 'b':
            b -= 1
    if i - j > beauty:
        beauty = i - j
print(beauty)
