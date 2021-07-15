S = input()
T = input()

S = S + T[-1]
if S == T:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
