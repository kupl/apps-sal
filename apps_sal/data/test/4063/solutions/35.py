n = int(input())
d = list(map(int, input().split()))

d = sorted(d, reverse=True)
cent_index = int(n/2)-1

print(d[cent_index] - d[cent_index+1])
