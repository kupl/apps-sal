n = int(input())
t = input()

ans = 10**10
if t == '0': print(ans); return
if t == '1': print((ans * 2)); return
if t == '11': print(ans); return
if t == '10': print(ans); return
if t == '01': print((ans - 1)); return
if t == '00': print((0)); return

l = 0; r = n  # M=[l,r)
if t[:3] == '110': l = 3
elif t[:3] == '101': l = 2
elif t[:3] == '011': l = 1
else: print((0)); return

if t[n - 3:] == '110': r = n
elif t[n - 3:] == '101': r = n - 1
elif t[n - 3:] == '011': r = n - 2
else: print((0)); return

L = t[:l]; M = t[l:r]; R = t[r:]

if len(M) % 3: print((0)); return
for i in range(len(M) // 3):
    if M[i * 3: i * 3 + 3] != '110': print((0)); return

S = '110110'; LR = L + R
ans -= 2 + len(M) // 3
for l in range(6):
    if S[l:l + len(LR)] == LR: ans += 1
print(ans)
