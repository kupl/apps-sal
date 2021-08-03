N, T = list(map(int, input().split()))
ct = [9999]
for _ in range(N):
    ctt = list(map(int, input().split()))
    if ctt[1] <= T:
        ct.append(ctt[0])
if ct == [9999]:
    print("TLE")
    return
print((min(ct)))
