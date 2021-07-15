def LI():
    return list(map(int, input().split()))


A, B, C = LI()
if A+B >= C:
    ans = "Yes"
else:
    ans = "No"
print(ans)

