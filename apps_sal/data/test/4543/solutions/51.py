a, b = map(str, input().split())
ans = "No"
key = int(a+b)
for i in range(1000):
    if i**2 == key:
        ans ="Yes"
        break
print(ans)
