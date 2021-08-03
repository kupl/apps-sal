T = int(input())
C = [60, 90, 108, 120, 135, 140, 144, 150, 156, 160, 162, 165, 168, 170, 171, 172, 174, 175, 176, 177, 178, 179]
Ans = ""
for t in range(T):
    n = int(input())
    if(n in C):
        Ans += "YES\n"
    else:
        Ans += "NO\n"
print(Ans, end="")
