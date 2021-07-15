n = int(input())
A = list(map(int, input().split()))
B = [abs(a) for a in A]
print(sum(B))
