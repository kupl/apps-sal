n = int(input())
k = sorted(map(int, input().split()))
for i in range(n - 2):
    if (k[i] + k[i + 1] > k[i + 2]):
        print("YES")
        break
else:
    print("NO")
