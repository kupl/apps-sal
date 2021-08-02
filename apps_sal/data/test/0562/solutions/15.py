n = int(input())
a, b = [], []
for i in range(n):
    t = [int(i) for i in input().split()]
    a.append(t[0])
    b.append(t[1])
a.sort()
b.sort()
i = j = 0
ans = 0

while ans <= 2 and i < n and j < n:
    """
    print(a[i],b[j])
    print(i,j,'\n')
    """
    if a[i] <= b[j]:
        ans += 1
        i += 1
    else:
        ans -= 1
        j += 1

if ans > 2: print("NO")
else: print("YES")
