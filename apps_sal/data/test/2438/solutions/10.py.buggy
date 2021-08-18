n = int(input())
s = input()
arr = []
for i in range(n):
    c = 0 if s[i] == 'A' else 1
    if not arr or arr[-1][0] != c:
        arr.append([c, 1])
    else:
        arr[-1][1] += 1
cnt = (n * n + n) // 2
if len(arr) == 1:
    print(cnt - n)
    return
for i in range(0, len(arr)):
    cnt -= arr[i][1] + (arr[i][1] if i != 0 and i != len(arr) - 1 else 0)
print(cnt - n + len(arr) - 1)
