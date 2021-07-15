s = input()
m = int(input())
calc = [0]
out = []
for i in range(1, len(s)):
    count = calc[i-1]
    if s[i] == s[i-1]:
        count += 1
    calc.append(count)
    
for q in range(m):
    L = [int(it) for it in input().split()]
    l, r, count = L[0] - 1, L[1] - 1, 0
    out.append(calc[r] - calc[l])
for c in out:
    print(c)

