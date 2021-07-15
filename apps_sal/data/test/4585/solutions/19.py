n=int(input())
ans = 0
Ans = 1

while ans < n:
    ans += Ans
    Ans += 1
print(Ans-1)
