k,s=map(int, input().split())
print(sum(s-k<=x+y<=s for x in range(min(k+1,s+1)) for y in range(min(k+1,s-x+1))))
