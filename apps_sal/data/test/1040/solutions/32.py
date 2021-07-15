l = int(input())
text = input()
tgt, ans = 'fox', ''

for i in range(l):
    ans += text[i]
    if ans[-3:] == tgt:
        ans = ans[:-3]
print(len(ans))
