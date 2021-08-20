s = str(input())
k = int(input())
wlist = [int(w) for w in input().split()]
letter = max(wlist)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
summ = 0
for i in range(len(s)):
    summ += wlist[alphabet.index(s[i])] * (i + 1)
print(summ + letter * (k * len(s) + (k + k ** 2) // 2))
