n, a, b = map(int, input().split())
r = 0
for i in range(n + 1):
    c = 0
    j = i
    for k in range(5):
        c += j % 10
        j = j//10
    if a <= c and c <= b:
        r += i

    
print(r)
