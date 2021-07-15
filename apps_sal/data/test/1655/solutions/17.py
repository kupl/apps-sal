n = int(input())
val = list(map(int, input().split()))
alive = 0
mn = n
for i in reversed(list(range(n))):
    if mn == i+1:
        alive += 1
        mn = i - val[i]
    else:
        mn = min(mn, i-val[i]) if i - val[i] >= 0 else 0
print(alive)


