A = list(map(int, input().split()))

even = []
odd = []
for i in range(3):
    if A[i] % 2 == 0:
        even.append(A[i])
    else:
        odd.append(A[i])

ans = 0

if len(even) == 3:
    even.sort(reverse=True)
    ans += (even[0] - even[1]) // 2
    ans += (even[0] - even[2]) // 2
elif len(even) == 2:
    even.sort(reverse=True)
    if odd[0] < even[0]:
        ans += -((-(even[0] - odd[0])) // 2)
        odd[0] += 2 * ans

    ans += (even[0] - even[1]) // 2
    ans += odd[0] - even[0]

elif len(even) == 1:
    odd.sort(reverse=True)
    if even[0] < odd[0]:
        ans += -((-(odd[0] - even[0])) // 2)
        even[0] += 2 * ans

    ans += (odd[0] - odd[1]) // 2
    ans += even[0] - odd[0]

else:
    odd.sort(reverse=True)
    ans += (odd[1] - odd[2]) // 2
    ans += (odd[0] - odd[1])

print(ans)
