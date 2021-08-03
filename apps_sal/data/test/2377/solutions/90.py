N, H = list(map(int, input().split()))
A = []
B = []
for i in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)
A_sorted = sorted(A, reverse=True)
B_sorted = sorted(B, reverse=True)

ans = 0
attack_sum = 0
for i in range(N):
    if B_sorted[i] >= A_sorted[0]:
        if H > attack_sum:
            attack_sum += B_sorted[i]
            ans += 1
        else:
            print(ans)
            return
    else:
        break
ans += - (-(H - attack_sum) // A_sorted[0])
print(ans)
