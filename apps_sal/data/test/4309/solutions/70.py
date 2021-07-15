N = int(input())
S = str(N)
x = int(S[0])
y = int(S[1])
z = int(S[2])
if x > y:
    ans = x*100+x*10+x
elif x < y:
    x += 1
    ans = x*100+x*10+x
else:
    if x > z:
        ans = x*100+x*10+x
    elif x < z:
        x += 1
        ans = x*100+x*10+x
    else:
        ans = N
print(ans)

