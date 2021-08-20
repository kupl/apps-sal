n = int(input())
s = str(input())
dict1 = {}
arr = list(map(int, input().split()))
for i in range(1, 10):
    dict1[i] = arr[i - 1]
ans = ''
i = 0
while i < n:
    if dict1[int(s[i])] > int(s[i]):
        break
    else:
        ans += s[i]
        i += 1
while i < n:
    if dict1[int(s[i])] < int(s[i]):
        break
    else:
        ans += str(dict1[int(s[i])])
        i += 1
ans += s[i:]
print(ans)
