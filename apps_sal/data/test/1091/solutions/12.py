n = int(input())
prs = [int(x) for x in input().split()]

print(prs.index(max(prs))+1, sorted(prs)[-2])
