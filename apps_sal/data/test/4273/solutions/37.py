N = int(input())
A = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
for i in range(N):
    s = input()
    if s[0] in A:
        A[s[0]] += 1
B = [A['M'], A['A'], A['R'], A['C'], A['H']]
ans = 0
for i in range(3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            ans += B[i] * B[j] * B[k]
print(ans)
