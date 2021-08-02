n = int(input())

m_wins = 0
c_wins = 0

for i in range(n):
    z1, z2 = list(map(int, input().split()))
    if z1 > z2:
        m_wins += 1
    elif z2 > z1:
        c_wins += 1

if m_wins > c_wins:
    print("Mishka")
elif c_wins > m_wins:
    print("Chris")
else:
    print("Friendship is magic!^^")
