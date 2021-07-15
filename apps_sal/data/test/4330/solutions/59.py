def LI():
    return list(map(int, input().split()))


A, B = LI()
if (A+B) % 2 == 0:
    ans = (A+B)//2
else:
    ans = "IMPOSSIBLE"
print(ans)

