n = int(input())
if n % 2 == 1:
    print(0)
    return
#### n is even ####
ans = 0
cnt = 0
ones = 0
keta = []
cnt = 5 * 2
while n >= cnt:
    ans += n // cnt
    cnt *= 5

print(ans)
