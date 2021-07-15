n , m = tuple(map(int, input().split()))
l = [list(map(int, input().split())) for i in range(n)]
mins = [min(l[i]) for i in range(n)]
print(max(mins))
