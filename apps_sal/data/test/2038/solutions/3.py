n =  int(input())
b = list((list(map(int, input().split()))))

a = list(zip(b,list(range(n))))

a.sort()

a = dict(a)

swaps = []

def swap(i, j):
    if i==j:
        return []
    if 2*(abs(i-j))  >= n:
        return [(i, j)]
    ans = []

    ii  = i
    jj = j
    if i < n//2:
        ans.append((i, n-1))
        ii = n-1
    if j>=n//2:
        ans.append((j, 0))
        jj = 0

    ans.append((ii, jj))

    if i < n//2:
        ans.append((i, n-1))
    if j>=n//2:
        ans.append((j, 0))

    return ans

#print(a)
ans = []
for i in range(n):
    ans.extend(swap(i, a[i+1]))

    t =b[i]
    b[i] = b[a[i+1]]
    b[a[i+1]] = t
    a[t]  = a[i+1]
    a[i+1] =  i
#print(a)
print(len(ans))
for k in ans:
    print(k[0]+1, k[1] +1)

