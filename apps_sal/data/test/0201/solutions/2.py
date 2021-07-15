a, b, c, d, e = list(map(int, input().split(' ')))
check = int(a**0.5)

#red candy
#height b
#weight d

#blue candy
#height c
#weight e

ans = 0
for red in range(check+1):
    blue = (a-d*red)//(e)
    if blue >= 0:
        ans = max(ans, red*b+blue*c)

for blue in range(check+1):
    red = (a-e*blue)//(d)
    if red >= 0:
        ans = max(ans, red*b+blue*c)

print(ans)
