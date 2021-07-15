l = input().split('metal')
ans = cur = 0
for str in l:
    cur += str.count('heavy')
    ans += cur
print(ans - cur)
