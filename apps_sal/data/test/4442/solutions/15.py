a, b = map(int,input().split())

ab = str(a) * b
ba = str(b) * a

if ab > ba:
    ans = ba
else:
    ans = ab

print(ans)
