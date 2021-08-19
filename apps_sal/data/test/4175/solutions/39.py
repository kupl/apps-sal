n = int(input())
w = [input() for _ in range(n)]
words = set()
ok = True
for i in range(n):
    if w[i] in words:
        ok = False
        break
    elif i != 0 and w[i - 1][-1] != w[i][0]:
        ok = False
        break
    words.add(w[i])
print('Yes' if ok else 'No')
