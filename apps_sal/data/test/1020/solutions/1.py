w, h, k = list(map(int, input().split()))
p = (w + h) * 2 - 4
res = 0

for i in range(k):
    res += p
    p -= 16
    
print(res)

