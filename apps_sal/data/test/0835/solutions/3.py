st = input()
B = st.count('B')
S = st.count('S')
C = st.count('C')
b, s, c = map(int, input().split())
bp, sp, cp = map(int, input().split())
r = int(input())
lm = 0
rm = int(1e15) + 1
while rm - lm > 1:
    m = (rm + lm) // 2
    bb = max(m * B - b, 0)
    ss = max(m * S - s, 0)
    cc = max(m * C - c, 0)
    if bp * bb + ss * sp + cc * cp <= r:
        lm = m
    else:
        rm = m
print(lm)
