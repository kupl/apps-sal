s=input()
prev=-1
ans=1
for x in s:
    if prev=='cons' and  x not in 'aeiou':
        ans=0
    if x in 'aeioun':
        prev='vow'
    else:
        prev='cons'
if prev=='cons':
    ans=0
print("YES" if ans else "NO")
