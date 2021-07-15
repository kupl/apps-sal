n = int(input())
s = input()
baz = ['RGB','RBG','GBR', 'GRB', 'BRG', 'BGR']
for i in range(len(baz)):
    baz[i] = (baz[i] * n)[0:n]
ans = 10 ** 9
text = baz[0]
for i in baz:
    ch = 0
    for j in range(n):
        if s[j] != i[j]:
            ch += 1
    if ch < ans:
        text = i
    ans = min(ans, ch)
print(ans)
print(text)
