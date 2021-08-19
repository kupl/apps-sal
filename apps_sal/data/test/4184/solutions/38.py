N = int(input())
W = list(map(int, input().split()))
S1 = 0
S2 = sum(W)
diff_min = sum(W)
for i in W:
    S1 += i
    S2 -= i
    diff = abs(S2 - S1)
    if diff < diff_min:
        diff_min = diff
    if S2 - S1 <= 0:
        break
print(diff_min)
