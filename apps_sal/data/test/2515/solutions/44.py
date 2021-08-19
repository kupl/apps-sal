MAX = 101010
is_prime = [True] * MAX
is_prime[0] = False
is_prime[1] = False
for i in range(2, MAX):
    if is_prime[i] == False:
        continue
    for j in range(i * 2, MAX, i):
        is_prime[j] = False
a = [0] * MAX
for i in range(MAX):
    if i % 2 == 0:
        continue
    if is_prime[i] and is_prime[(i + 1) // 2]:
        a[i] = 1
s = [0]
for x in a:
    s.append(s[-1] + x)
Q = int(input())
for _ in range(Q):
    (l, r) = list(map(int, input().split()))
    print(s[r + 1] - s[l])
