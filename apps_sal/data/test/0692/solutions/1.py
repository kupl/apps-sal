n = int(input())
mod = list(map(int, input().split()))
rem = list(map(int, input().split()))
cnt = 0
for d in range(360360):
    we = False
    for (r, m) in zip(rem, mod):
        if d % m == r:
            we = True
            break
    if we:
        cnt += 1
print(cnt / 360360)
