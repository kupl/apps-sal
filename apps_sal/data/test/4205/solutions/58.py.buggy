# ABC135

N = int(input())
P = list(map(int, input().split()))
sorted_P = sorted(P)
cnt = 0
for i in range(len(P)):
    if P[i] != sorted_P[i]:
        cnt += 1

    if cnt > 2:
        print("NO")
        return
print("YES")
