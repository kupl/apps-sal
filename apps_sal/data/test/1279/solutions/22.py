n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
odd1 = odd2 = even1 = even2 = 0
for i in a:
    if i%2: odd1+=1
    else: even1+=1
for i in b:
    if i%2: odd2+=1
    else: even2+=1
print(min(odd1, even2)+min(odd2, even1))

