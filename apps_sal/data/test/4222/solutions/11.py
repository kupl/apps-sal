(n, k) = list(map(int, input().split()))
A = []
A_dup = []
cnt = 0
for i in range(k):
    input()
    A_dup += list(map(int, input().split()))
A_eldup = list(set(A_dup))
for i in range(1, n + 1):
    if i not in A_eldup:
        cnt += 1
print(cnt)
