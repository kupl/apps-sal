n = int(input())
k = sorted(map(int, input().split()))
j = -1
for i in range(n):
    print(k[i], k[j])
    j -= 1

