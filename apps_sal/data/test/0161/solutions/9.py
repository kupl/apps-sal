x = int(input())
prop = {2**i - 1 for i in range(1, 40)}
ans = 0
Ans = []
while x not in prop:
    j = x.bit_length()
    ans += 1
    Ans.append(j)
    x ^= (1 << j) - 1
    if x in prop:
        break
    x += 1
    ans += 1
print(ans)
if ans:
    print(*Ans)
