import math

n = int(input())

a = [int(i) for i in input().split(" ")]
ar = a[::-1]
a = [0] + a
ar = [0] + ar
s = [0] * (n + 1)
sr = [0] * (n + 1)
li = 0
ri = n

for i in range(1, n + 1):
    s[i] = a[i] + s[i - 1]
    sr[i] = ar[i] + sr[i - 1]
    
def f(a):
    return max(a) - min(a)

def fs(rr):
    nonlocal li
    while abs(s[rr] - 2 * s[li]) > abs(s[rr] - 2 * s[li + 1]):
        li += 1
        
def fsr(rr):
    nonlocal ri
    while abs(sr[rr] - 2 * sr[ri]) > abs(sr[rr] - 2 * sr[ri - 1]):
        ri -= 1

m_min = 2 * 10**14
for i in range(2, n - 1):
    fs(i)
    fsr(n - i)
    m = f([s[li], s[i] - s[li], sr[ri], sr[n - i] - sr[ri]])
    if m < m_min:
        m_min = m
        
print(m_min)
