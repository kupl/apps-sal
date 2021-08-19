s = list(input())
t = list(input())
ans = 'No'
for i in range(len(s) + 1):
    if s[-i:] + s[:len(s) - i] == t:
        ans = 'Yes'
print(ans)
