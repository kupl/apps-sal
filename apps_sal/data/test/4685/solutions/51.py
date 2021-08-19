mylists = list(map(int, input().split()))
k = int(input())
mylists.sort(reverse=True)
print(mylists[0] * 2 ** k - mylists[0] + sum(mylists))
