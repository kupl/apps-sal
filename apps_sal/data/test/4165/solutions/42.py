N = int(input())

p = list(map(int, input().split()))

print("Yes" if max(p) < sum(p)- max(p) else "No")
