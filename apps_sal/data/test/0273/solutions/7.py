a,b = input().split()
print(min(a[:i+1]+b[:j+1] for i in range(len(a)) for j in range(len(b))))

