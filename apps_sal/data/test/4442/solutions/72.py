a, b = map(int, input().split())

ab = str(a) * b
ba = str(b) * a

if ab > ba:
    answer = ba
else:
    answer = ab
    
print(answer)
