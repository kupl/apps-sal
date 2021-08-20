(n, k) = map(int, input().split())
t = input()
cycle = n
for i in range(1, n):
    if t[i:] == t[:n - i]:
        cycle = i
        break
ans = t[:cycle] * k + t[cycle:]
print(ans)
