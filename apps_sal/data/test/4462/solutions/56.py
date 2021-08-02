N = int(input())
A = list(map(int, input().split()))

two = 0
four = 0
odd = 0

for a in A:
    if a % 4 == 0:
        four += 1
    elif a % 2 == 0:
        two += 1

N -= max(0, two - 1)

print("Yes" if four >= N // 2 else "No")
