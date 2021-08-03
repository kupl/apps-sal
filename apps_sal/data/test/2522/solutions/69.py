from collections import Counter


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C_A = Counter(A)
C_B = Counter(B)
for k, v in list(C_A.items()):
    if v + C_B[k] > N:
        print("No")
        return
B = B[::-1]
same_range = []
for i, (a, b) in enumerate(zip(A, B)):
    if a == b:
        same_range.append(i)
if same_range:
    same_v = B[same_range[0]]
    for i in range(N):
        if not same_range:
            break
        if A[i] == same_v or B[i] == same_v:
            continue
        j = same_range.pop()
        B[i], B[j] = B[j], B[i]
print("Yes")
print((" ".join(map(str, B))))
