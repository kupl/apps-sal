a, b, c = map(int, input().split())
k = int(input())

if max([a,b,c]) == c:
    ans = c*(2**k) + b + a
elif max([a,b,c]) == b:
    ans = b*(2**k) + a + c
else:
    ans = a*(2**k) + b + c
print(ans)
