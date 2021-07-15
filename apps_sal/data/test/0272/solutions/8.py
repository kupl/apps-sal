s = input()
t = input()
let = {}
printed = []
f = True
ans = 0
if s == t:
    print(0)
else:
    for i in range(len(s)):
        if s[i] in let:
            if t[i] != let[s[i]]:
                print(-1)
                f = False
                break
        elif t[i] in let:
            if s[i] != let[t[i]]:
                print(-1)
                f = False
                break
        else:
            if s[i] != t[i] and (s[i] not in let or t[i] not in let):
                ans += 1
            let[s[i]] = t[i]
            let[t[i]] = s[i]
    if f:
        print(ans)
        for l in let:
            if let[l] != l and let[l] not in printed:
                print(let[l], l)
                printed.append(l)

