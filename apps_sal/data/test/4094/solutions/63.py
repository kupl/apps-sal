k = int(input())
seven = 7
ans = -1

for i in range(1,k+1):
    seven %= k
    if seven  == 0:
        ans = i
        break
    else:
        seven = seven * 10 + 7

print(ans)
