

def R():
    return list(map(int, input().strip().split()))


n = int(input())
possible = [1, 1, 0]
pos = True
for i in range(n):
    a = int(input())
    if possible[a - 1] != 1:
        pos = False
    for j in range(3):
        if possible[j] == 1 and a != j + 1:
            possible[j] = 0
            continue
        if possible[j] == 0:
            possible[j] = 1

if pos:
    print("YES")
else:
    print("NO")
