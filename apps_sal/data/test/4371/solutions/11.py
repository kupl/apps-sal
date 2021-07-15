S = input()

lst = []
ans = 1000
for n in range(3, len(S)+1):
    i = int(S[n-3:n])
    lst.append(i)

for m in lst:
    d = abs(753 - m)
    if ans > d:
        ans = d
    
print(ans)
