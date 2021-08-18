n, k, c = map(int, input().split())
s = input()
forth = set()
reverse = set()
cur = 0
tired = 0
for i in range(n):
    if s[i] == "o":
        if tired == 0:
            cur += 1
            tired = c
            forth.add(i + 1)
        else:
            if tired > 0:
                tired -= 1
    else:
        if tired > 0:
            tired -= 1
if cur > k:
    return
s = s[::-1]
cur = 0
tired = 0
for i in range(n):
    if s[i] == "o":
        if tired == 0:
            cur += 1
            tired = c
            reverse.add(n - i)
        else:
            if tired > 0:
                tired -= 1
    else:
        if tired > 0:
            tired -= 1
ans = forth & reverse
ans = list(ans)
ans.sort()
for i in ans:
    print(i)
