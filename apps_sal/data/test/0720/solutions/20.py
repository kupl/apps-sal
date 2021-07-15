n = int(input())
last = 0
total = 1
for _ in range(n):
    a,b = list(map(int,input().split()))
    min_score = min(a,b)
    max_score = max(a,b)
    if min_score > last:
        total += (min_score-last)  
    if a == b:
        last = a
    else:
        last = max(0,max_score-1)
print(total)

