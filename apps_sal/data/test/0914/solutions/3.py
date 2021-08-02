s = input()
n = int(input())

symb_cnt = {}
for c in s:
    symb_cnt[c] = symb_cnt[c] + 1 if c in symb_cnt else 1
for cnt in range(1, len(s) + 1):
    s1 = ""
    for c in symb_cnt:
        s1 += c * ((symb_cnt[c] + cnt - 1) // cnt)
    if len(s1) <= n:
        for i in range(n - len(s1)):
            s1 += 'a'
        print(cnt)
        print(s1)
        return
print(-1)
