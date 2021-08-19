n = int(input())
c = [int(s) for s in input().split(' ')]
C_rev = c[0]
C_nrev = 0
last_s = input()
last_s_rev = last_s[::-1]
for i in range(1, n):
    s = input()
    s_rev = s[::-1]
    new_C_nrev = float('inf')
    if last_s <= s:
        new_C_nrev = min(new_C_nrev, C_nrev)
    if last_s_rev <= s:
        new_C_nrev = min(new_C_nrev, C_rev)
    new_C_rev = float('inf')
    if last_s <= s_rev:
        new_C_rev = min(new_C_rev, C_nrev + c[i])
    if last_s_rev <= s_rev:
        new_C_rev = min(new_C_rev, C_rev + c[i])
    if min(C_rev, C_nrev) == float('inf'):
        break
    C_rev = new_C_rev
    C_nrev = new_C_nrev
    last_s = s
    last_s_rev = s_rev
print(-1 if min(C_rev, C_nrev) == float('inf') else min(C_rev, C_nrev))
