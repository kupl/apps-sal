a = int(input())
v = list(map(int, input().split()))
v.sort()
print(v[(a + 1) // 2 - 1])
