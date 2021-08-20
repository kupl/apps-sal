t = int(input())
for qwe in range(t):
    n = int(input())
    s = input()
    a = [i + 1 for i in range(len(s)) if s[i] == '1']
    if a == []:
        print(n)
        continue
    mx = a[-1]
    mn = a[0]
    ans = max(mx, n - mn + 1) * 2
    print(ans)
