def check(st):
    cnt = [st.count(ch) for ch in "UDRL"]
    return cnt[0] == cnt[1] and cnt[2] == cnt[3]

n = int(input())
s = input().strip()

ans = int(0)
for l in range(2, n+1):
    for i in range(0, n-l+1):
        if check(s[i:i+l]):
            ans += 1

print(ans)
