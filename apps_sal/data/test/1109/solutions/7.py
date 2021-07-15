n, k = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(k):
    s1, s2 = 0, 0
    for j in range(i, n, k):
        if A[j] == 1:
            s1+=1
        else:
             s2+=1
    ans = ans + min(s1, s2)
print(ans)
