s = int(input(), base=2)
#print(s)
k = 0
ans = 0
while 4 ** k < s:
    ans += 1
    k += 1
print(ans)
