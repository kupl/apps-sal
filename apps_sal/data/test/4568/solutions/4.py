n = int(input())
s = input()
ans = 0
for i in range(n-1):
    front = set(s[:i+1])
    back = set(s[i+1:])
    ans = max(ans, len(front&back))
print(ans)
