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
i = 0
while same_range:
    v = B[same_range[0]]
    if A[i] != v and B[i] != v:
        j = same_range.pop()
        B[i], B[j] = B[j], B[i]
    i += 1
print("Yes")
print((" ".join(map(str, B))))

