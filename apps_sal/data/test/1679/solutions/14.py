n = input()
a = list(map(str, input().split('0')))
ans = ""
for i in a:
    ans += str(len(i))
print(ans)
