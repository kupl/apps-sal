from string import ascii_uppercase as au
N = int(input())
S = input()
ans = ''
for s in S:
    idx = (au.index(s) + N) % len(au)
    ans += au[idx]
print(ans)
