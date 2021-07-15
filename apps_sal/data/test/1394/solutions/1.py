a = input()
c = a.count('a')
new = a.replace('a', '')
k = len(new)
if k % 2 == 0 and new[:k//2] == new[k//2:] and a[:k//2+c].count('a') == c:
    print(a[:k//2+c])
else:
    print(":(")
