k = int(input())
s = input()
if k >= len(s):
    print(s)
else:
    s = s[:k] + '...'
    print(s)
