S = list(input())
S = list(set(S))

ans = "None"
for i in range(97, 123):
    cnt = chr(i)
    if not cnt in S:
        ans = cnt
        break
        
print(ans)
