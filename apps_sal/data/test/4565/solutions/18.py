n = int(input())
s = input()
arr = []
E = s.count('E')
w = 0
e = 0
for i in range(n):
    if s[i] == 'W':
        arr.append(w + E - e)
        w += 1
    else:
        arr.append(w + E - e - 1)
        e += 1
ans = min(arr)
print(ans)
