N = int(input())
A = list(map(int, input().split()))
A.sort()

pre = 0
ans = 0
for a in A:
    if a > pre+1:
        ans += 1
        pre = a-1
    elif a > pre:
        ans += 1
        pre = a
    elif a == pre:
        ans += 1
        pre = a+1
print(ans)
