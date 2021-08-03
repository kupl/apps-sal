n = int(input())
vols = list(map(int, input().split()))
caps = map(int, input().split())
max = list(sorted(caps))[-2:]
if sum(vols) <= sum(max):
    print("YES")
else:
    print("NO")
