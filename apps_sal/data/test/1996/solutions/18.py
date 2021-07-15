n = int(input())
let = set()
for i in range(97, 123):
    let.add(chr(i))
flag = 0
ans = 0
for i in range(n - 1):
    if len(let) == 1:
        flag = 1
    t, s = map(str, input().split())
    #print(t, s)
    if t == '!':
        now = set(list(s))
        if flag == 1:
            ans += 1
        let = let.intersection(now)
        #print(now)
        #print(let)
    if t == '?':
        if flag == 1:
            ans += 1
        if s in let:
            let.remove(s)
    if t == '.':
        now = list(s)
        for elem in now:
            if elem in let:
                let.remove(elem)
print(ans)
