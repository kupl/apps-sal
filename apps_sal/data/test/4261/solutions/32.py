A,B,C = map(int,input().split())
if B + C > A:
    ans = C - (A - B)
else:
    ans = 0
print(ans)
