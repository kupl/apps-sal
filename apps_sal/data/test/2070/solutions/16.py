arr = list(map(int, input().split()))
astr = input()
length = len(astr)

ans = 0
tsum = 0
st = {}

for i in range(length):
    st.setdefault(astr[i], {})
    ans += st[astr[i]].get(tsum, 0)
    tsum += arr[ord(astr[i]) - 97]
    st[astr[i]][tsum] = st[astr[i]].get(tsum, 0) + 1

print(ans)
