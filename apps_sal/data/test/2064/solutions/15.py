inpt = int(input())
ans = ""
if inpt & 1 == 1:
    inpt = inpt - 3
    ans = "7"
ans += "1" * (inpt >> 1)
print(ans)
