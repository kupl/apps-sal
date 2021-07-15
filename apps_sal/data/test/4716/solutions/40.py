N_hon, K_part = map(int, input().split())
length = list(map(int, input().split()))

length.sort()
ans = sum(length[-K_part:])

print(ans)
