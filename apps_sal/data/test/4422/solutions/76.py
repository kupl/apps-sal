n, k = map(int, input().split())
s = input()

ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
abc = 'abcdefghijklmnopqrstuvwxyz'
print(s[:k-1] + abc[ABC.index(s[k-1])] + s[k:])
