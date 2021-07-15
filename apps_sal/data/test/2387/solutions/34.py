import sys
readline = sys.stdin.readline

N = int(readline())
S = [readline().rstrip() for _ in range(N)]

def count_cb_ob(s):
    st = []
    for i, si in enumerate(s):
        if si == '(' or len(st) == 0 or st[-1] != '(':
            st.append(si)
        else:
            st.pop()
    return st.count(')'), st.count('(')

cb_obs = map(count_cb_ob, S)
f, b, s = [], [], []
for down, up in cb_obs:
    (f if down < up else (s if down == up else b)).append((down, up))

f = sorted(f)
b = sorted(b, key=lambda x:x[1], reverse=True)

count = 0
ans = 'Yes'
for down, up in (*f, *s, *b):
    count -= down
    if count < 0:
        ans = 'No'
    count += up

if count != 0:
    ans = 'No'

print(ans)
