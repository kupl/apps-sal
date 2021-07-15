N = int(input())
ans = 0
lst = [0]*100
 
for i in range(1, N+1):
    A = str(i)
    a, b = A[0], A[-1]
 
    if b == '0':
        pass
 
    else:
        lst[int(b+a)] += 1
 
for i in range(1, N+1):
    A = str(i)
    a, b = A[0], A[-1]
    c = int(a+b)
    ans += lst[c]
 
print(ans)
