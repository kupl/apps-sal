N = int(input())
A = list(map(int, input().split()))
ans = 0
is_end = False
while True:
    for a in A:
        if a % 2 != 0:
            is_end = True
            break
    if is_end:
        break
    ans += 1
    A = [a / 2 for a in A]

print(ans)
