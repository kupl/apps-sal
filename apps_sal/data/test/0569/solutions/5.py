n = int(input())
s = input()
ans = n - len(set(s))
if n > 26: ans = -1
print(ans)

