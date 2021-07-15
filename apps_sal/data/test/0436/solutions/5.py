n = int(input())
a = list(map(int, input().split()))

sol = [1]
s = a[0]

for i in range(1, n):
    if a[i]*2<=a[0]:
        sol.append(i+1)
        s+=a[i]
if s>sum(a)//2:
    print(len(sol))
    print(*sol)
else:
    print(0)

