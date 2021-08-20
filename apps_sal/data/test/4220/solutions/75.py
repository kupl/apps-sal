k = int(input())
s = input()
l = len(s)
if l > k:
    print(s[0:k] + '...')
else:
    print(s)
