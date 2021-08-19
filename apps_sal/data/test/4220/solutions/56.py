k = int(input())
s = str(input())
if len(s) > k:
    s = s[:k] + '...'
print(s)
