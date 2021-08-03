n = int(input())
ok = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    if a == b:
        ok = ok + 1
if ok == n:
    print("Poor Alex")
else:
    print("Happy Alex")
