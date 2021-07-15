n = int(input())
l = list(map(int, input().split()))

sort_l = sorted(l)

print(sum(sort_l[-2::-2]))
