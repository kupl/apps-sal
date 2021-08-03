S = input()
ans = "First"
if (S[0] == S[-1]) ^ (len(S) % 2 == 0):
    ans = "Second"
print(ans)
