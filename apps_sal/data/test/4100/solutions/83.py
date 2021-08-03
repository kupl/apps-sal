N, K, Q = [int(n) for n in input().split()]
l = [0] * N
for i in range(Q):
    l[int(input()) - 1] += 1

ans = ['Yes' if K + v - Q > 0 else 'No' for v in l]

for a in ans:
    print(a)
