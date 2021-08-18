a, b, c = map(int, input().split())
ans = abs(b - a) + abs(c - b)
ans2 = abs(c - a) + abs(b - c)
if(ans2 < ans):
    ans = ans2
ans2 = abs(a - b) + abs(c - a)
if(ans2 < ans):
    ans = ans2
ans2 = abs(c - b) + abs(a - c)
if(ans2 < ans):
    ans = ans2
ans2 = abs(a - c) + abs(b - a)
if(ans2 < ans):
    ans = ans2
ans2 = abs(b - c) + abs(a - b)
if(ans2 < ans):
    ans = ans2
print(ans)
