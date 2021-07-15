from collections import Counter
s = list(input())
n = len(s)
c = Counter(s)
mod = 10**9+7


left_a  = 0
left_b  = 0
left_c  = 0
left_q  = 0
right_a = c['A']
right_b = c['B']
right_c = c['C']
right_q = c['?']

def add_ans():
    lhs = left_a * pow(3, left_q, mod) + left_q*pow(3, left_q-1, mod)
    rhs = right_c * pow(3, right_q, mod) + right_q*pow(3, right_q-1, mod)
    return  (lhs * rhs)%mod

ans = 0
for i in range(n):
    if s[i] == 'A':
        left_a  += 1
    if s[i] == 'B':
        ans = (ans+ add_ans())%mod
    if s[i] == 'C':
        right_c -= 1
    if s[i] == '?':
        right_q -= 1
        ans = (ans+ add_ans())%mod
        left_q  += 1
print(ans)


