[n] = [int(i) for i in input().split()]
li = [int(i) for i in input().split()]
ans = 0
for i in li:
    ans += i
print(ans - n)
