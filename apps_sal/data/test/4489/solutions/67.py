N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]
Get = {}
for s in S:
    if s in Get:
        Get[s] += 1
    else:
        Get[s] = 1
for t in T:
    if t in Get:
        Get[t] += -1
    else:
        Get[t] = -1
ans = max(Get.values())
print(ans if ans > 0 else 0)
