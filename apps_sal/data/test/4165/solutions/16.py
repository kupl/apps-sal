N = int(input())
edge = list(map(int, input().split()))
if max(edge) < sum(edge) - max(edge):
    print("Yes")
else:
    print("No")
