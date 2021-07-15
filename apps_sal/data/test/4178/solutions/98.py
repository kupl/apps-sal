n = int(input())
h = list(map(int, input().split()))
ans = 'Yes'
if n != 1: 
    i = 0
    b = 0
    while i < n:
        if h[i] < b:
            ans = 'No'
            break
        b = max(b, h[i]-1)
        i += 1
print(ans)
