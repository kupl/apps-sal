n = int(input())
(*l,) = map(int, input().split())
odd = False
even = False
for x in l:
    if x % 2 == 0:
        even = True
    else:
        odd = True
if odd and even:
    l.sort()
print(*l)
